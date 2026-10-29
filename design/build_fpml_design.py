#!/usr/bin/env python3
"""Build native FPML source through the installed FigCraft loopback control protocol.
Run FigCraft --control 7979, then python3 design/build_fpml_design.py.
"""
import csv,json,socket,pathlib,argparse,base64
ROOT=pathlib.Path(__file__).resolve().parents[1]
P=argparse.ArgumentParser();P.add_argument('--port',type=int,default=7979);args=P.parse_args()
s=socket.create_connection(('127.0.0.1',args.port),timeout=60);f=s.makefile('rb');seq=0
def rpc(method,params={}):
 global seq
 seq+=1;s.sendall((json.dumps(dict(id=seq,method=method,params=params))+'\n').encode());r=json.loads(f.readline())
 if not r.get('ok'):raise RuntimeError(r)
 return r.get('result')
def cmd(command,**params):return rpc('engine.execute',dict(command=command,params=params))
BG='#101417';PANEL='#181E22';LINE='#2D363D';WHITE='#F4F7F5';MUTED='#A6B2B9';GREEN='#77C99B'
rows=list(csv.DictReader(open(ROOT/'predictions/latest.csv')));squad=json.load(open(ROOT/'squad.json'));owned={str(p['player_code']) for p in squad['players']};team=[r for r in rows if r['player_code'] in owned];team.sort(key=lambda r:(r['current_GW9_lineup']!='True',{'Goalkeeper':0,'Defender':1,'Midfielder':2,'Forward':3}[r['position']]))
manifest={};batch=[];n=0
def node(typ,name,x,y,w,h,parent=None,text=None,**props):
 global n;n+=1;ref='n'+str(n);p=dict(type=typ,name=name,x=x,y=y,width=w,height=h,props=props,select=False)
 if parent:p['parent']=parent
 if text is not None:p['text']=str(text)
 batch.append(dict(command='node.create',params=p,**{'as':ref}));return {'$ref':ref}
def text(p,t,x,y,w=300,size=16,color=WHITE):return node('text',str(t)[:55],x,y,w,24,p,text=t,fontFamily='IBM Plex Sans',fontSize=size,fill=color,textAutoResize='height',features={'tnum':True})
def box(p,name,x,y,w,h,fill=PANEL):return node('frame',name,x,y,w,h,p,fill=fill,clip=True)
def button(p,label,x,y,w=180):
 b=box(p,label,x,y,w,44,WHITE);text(b,label,14,10,w-24,14,BG);return b
def line(p,y,w):node('rectangle','Divider',0,y,w,1,p,fill=LINE)
def flush():
 global batch
 resolved={}
 def resolve(v):
  if isinstance(v,dict):
   if '$ref' in v:return resolved[v['$ref']]
   return {k:resolve(x) for k,x in v.items()}
  return v
 for step in batch:
  result=cmd(step['command'],**resolve(step['params']));resolved[step['as']]=result['id']
 batch=[];return result
def page(name):cmd('page.add',name=name)
def screen(name,w,x=0,h=1000):
 a=box(None,name,x,0,w,h,BG);text(a,'FPML',24 if w<768 else 48,24,200,24);text(a,'Forecasts / GW9–13',24 if w<768 else w-260,64 if w<768 else 30,240,13,MUTED)
 if w>=768:text(a,'Team      Players      Model',350,29,420,16)
 else:
  nav=box(a,'Bottom navigation',0,h-70,w,70,PANEL);text(nav,'Team             Players             Model',28,23,w-40,15)
 return a
def player(p,r,y,w,compact=False):
 text(p,r['web_name']+('  C' if r['current_GW9_captain']=='True' else '  VC' if r['current_GW9_vice_captain']=='True' else ''),0,y,w-100,16)
 text(p,r['team_short_name']+' · '+r['position'],0,y+24,w-100,12,MUTED)
 text(p,f"{float(r['GW9_predicted_points']):.1f}",w-50,y,50,18);line(p,y+55,w)
def team_screen(name,w,x=0,decision_first=False,state='Team'):
 a=screen(name,w,x,1640 if w<1024 else 1300);pad=24 if w<768 else 48;cw=w-2*pad;mobile=w<1024
 text(a,state,pad,112 if mobile else 112,cw,28);text(a,'Bank £1.0m    ·    15 players',pad,158,cw,14,MUTED)
 text(a,'GW9     GW10     GW11     GW12     GW13',pad,198,cw,14)
 sy=460 if mobile and decision_first else 260;sw=cw if mobile else 740
 squadpanel=box(a,'Current squad',pad,sy,sw,1000,BG);text(squadpanel,'Your XI / bench',0,0,sw,20)
 first=None
 for i,r in enumerate(team):
  rr=box(squadpanel,'Player '+r['player_code'],0,48+i*58,sw,58,BG);player(rr,r,0,sw);first=first or rr

 dx=pad if mobile else 868;dy=250;dw=cw if mobile else w-dx-pad
 d=box(a,'Decision panel',dx,dy,dw,184,PANEL);text(d,'Next move',20,16,dw-40,20);text(d,'Review available transfers',20,56,dw-40,16);text(d,'Weighted 5-GW XI + captain gain',20,86,dw-40,12,MUTED);preview=button(d,'Preview transfer',20,124,min(200,dw-40))
 if not mobile:button(a,'Edit team',w-220,112,172);text(a,'Other transfers  +',dx,465,dw,16);text(a,'Optimal comparison  +',dx,513,dw,16)
 return a,first,preview
rpc('ui.key',dict(key='Escape'))
cmd('file.new',name='FPML')
cmd('text.loadFont',path=str(ROOT/'design/IBMPlexSans.ttf'))
fonts=cmd('text.fonts');(ROOT/'design/font-index.json').write_text(json.dumps(fonts,indent=2))
tokens=cmd('variable.createCollection',name='FPML tokens')
for token,value in [('background',BG),('panel',PANEL),('divider',LINE),('text',WHITE),('muted',MUTED),('positive',GREEN)]:cmd('variable.create',collection=tokens['id'],name=token,type='color',value=value)
# Reusable native components, including text overrides inspected after re-opening.
page('Components')
for i,(name,w,h) in enumerate([('Player row',600,64),('Primary action',200,44),('Navigation',390,64),('Forecast strip',350,72),('Price field',260,72)]):
 c=node('component',name,0,i*130,w,h,fill=PANEL,layout='horizontal',gap=16,padding=16)
 text(c,{'Player row':'Gabriel       ARS · Defender       5.2','Primary action':'Calculate preview','Navigation':'Team     Players     Model','Forecast strip':'GW9    GW10    GW11    GW12    GW13\n5.2      6.9        5.2        5.0        5.2','Price field':'Bank / £1.0m'}[name],0,0,w-24,14)
flush()
page('Composition study')
team_screen('A / squad first / desktop',1440);team_screen('B / decision first / mobile',390,1520,True);flush()
page('Desktop')
desk,df,dp=team_screen('Team / desktop',1440); screens={'team-desktop':desk}
for idx,kind in enumerate(['Players','Model']):
 a=screen(kind+' / desktop',1440,(idx+1)*1520);screens[kind.lower()+'-desktop']=a;text(a,kind,48,112,900,28)
 if kind=='Players':
  text(a,'Forecasts      Recent form',48,164,700,16);text(a,'Search players                       Position      Club      Price      Owned',48,214,1250,16,MUTED)
  p=box(a,'Player ledger',48,280,1344,650,BG)
  for i,r in enumerate(rows[:9]):player(p,r,i*66,1300)
 else:
  text(a,'Live season / XI + captain vs FPL average',48,180,1100,20);text(a,'Before autosubs · frozen forecasts',48,216,1100,14,MUTED)
  text(a,'GW       Model XI + C       FPL average',48,280,1100,15,MUTED)
  for j,perf in enumerate(list(csv.DictReader(open(ROOT/'predictions/performance.csv')))[-8:]):text(a,perf['gameweek']+'                 '+perf['optimal_xi_captain_points']+'                     '+perf['fpl_average'],48,312+j*28,1100,16)
  for i,t in enumerate(['Live metrics  +','Historical evaluation  +','Data freshness  +','Model provenance  +','Assumptions and limits  +']):text(a,t,48,580+i*66,1100,18);line(a,622+i*66,1392)
flush()
page('Mobile')
mt,mf,mp=team_screen('Team / mobile',390,decision_first=True);screens['team-mobile']=mt
for idx,kind in enumerate(['Players','Model']):
 a=screen(kind+' / mobile',390,(idx+1)*460,1120);screens[kind.lower()+'-mobile']=a;text(a,kind,24,112,340,28)
 if kind=='Players':
  text(a,'Forecasts       Recent form',24,164,340,16);text(a,'Search players…     Filters',24,218,340,16,MUTED);p=box(a,'Player ledger',24,280,342,650,BG)
  for i,r in enumerate(rows[:9]):player(p,r,i*72,342)
 else:
  text(a,'XI + captain vs FPL average',24,180,342,20);text(a,'Before autosubs · frozen forecasts',24,240,342,13,MUTED)
  for i,t in enumerate(['Live results / completed GWs','Live metrics  +','Historical evaluation  +','Data freshness  +','Provenance and limits  +']):text(a,t,24,320+i*100,342,18)
flush()
# Resolve frame IDs from inspect by name after batches.
def tree():return rpc('document.inspect',dict(depth=20,allPages=True))
page('Layout checks')
for checkwidth in [320,768]:team_screen('Team / '+str(checkwidth),checkwidth,0 if checkwidth==320 else 420,True)
flush()
page('Flow and states')
flow=[]
for i,title in enumerate(['Player details','Transfer preview','Calculated preview','Saved current team','Loading','Hold','Invalid squad','Stale analysis','Save error']):
 a=screen(title,390,i*460,1000);flow.append(a);text(a,title,24,120,340,28)
 body={'Player details':team[0]['web_name']+'\nGW9  '+str(round(float(team[0]['GW9_predicted_points']),1))+'\nHistory coverage: '+team[0]['confidence'],'Transfer preview':'Draft · saved team unchanged\nChoose replacement and purchase price','Calculated preview':'Prototype result · not a live calculation\nReview changes before saving','Saved current team':'Saved\nCurrent team updated','Loading':'Connecting to analysis…','Hold':'Hold\nNo positive transfer available','Invalid squad':'15 players required\nReview your incomplete draft','Stale analysis':'Needs recalculation\nForecast changed','Save error':'Could not save\nYour draft is preserved'}[title]
 text(a,body,24,210,342,18);label='Preview transfer' if i==0 else 'Calculate preview' if i==1 else 'Save as current team' if i==2 else 'Back to team';b=button(a,label,24,430,342)
 # named hotspots are connected after resolving native IDs
 node('rectangle','Flow hotspot '+str(i),24,430,342,44,a,fill='none',pluginData={'fpml.flow':str(i)})
flush()
cmd('file.saveAs',path=str(ROOT/'design/FPML.figcraft'))
doc=tree();(ROOT/'design/inspection.json').write_text(json.dumps(doc,indent=2))
def walk(v):
 if isinstance(v,dict):
  if 'id' in v and 'name' in v:yield v
  for x in v.values():yield from walk(x)
 elif isinstance(v,list):
  for x in v:yield from walk(x)
ns=list(walk(doc));byname={v['name']:v['id'] for v in ns}
for i in range(9):
 target=['Transfer preview','Calculated preview','Saved current team','Team / mobile'][min(i,3)]
 cmd('proto.interaction.add',id=byname['Flow hotspot '+str(i)],dest=byname[target])
cmd('proto.interaction.add',id=byname['Team / mobile'],dest=byname['Player details'])
cmd('proto.flow.add',start=byname['Team / mobile'],name='Team → details → preview → save')
cmd('file.save');cmd('file.revert')
doc=tree();ns=list(walk(doc));byname={v['name']:v['id'] for v in ns}
for key in screens:
 name=key.split('-')[0].capitalize()+' / '+key.split('-')[1]
 rpc('ui.render',dict(ids=[byname[name]],path=str(ROOT/'design'/str(key+'.png')),scale=1))
cmd('page.select',id=next(p['id'] for p in doc['pages'] if p['name']=='Composition study'))
for name,key in [('A / squad first / desktop','composition-a'),('B / decision first / mobile','composition-b')]:rpc('ui.render',dict(ids=[byname[name]],path=str(ROOT/'design'/str(key+'.png'))))
for width in [320,768]:rpc('ui.render',dict(ids=[byname['Team / '+str(width)]],path=str(ROOT/'design'/str('team-'+str(width)+'.png'))))
cmd('file.save')
# Verify real component instance text overrides survive disk round-trip.
cmd('page.select',id=next(p['id'] for p in doc['pages'] if p['name']=='Components'))
instance=cmd('instance.create',component=byname['Primary action'],x=700,y=130)['id']
inst=rpc('node.get',dict(id=instance,depth=5))
textnode=next(v for v in walk(inst) if v.get('type')=='TEXT')
cmd('node.set',ids=[textnode['id']],props={'characters':'Save as current team'})
cmd('file.save');cmd('file.revert')
override=rpc('node.get',dict(id=instance,depth=5))
assert 'Save as current team' in json.dumps(override), 'Component override did not persist'
doc=tree();ns=list(walk(doc));byname={v['name']:v['id'] for v in ns}
# Structural checks remain available while the app is hidden by the host session.
links=[v for v in walk(doc) if v.get('interactions')]
assert len(links)>=10, 'Prototype links did not survive disk reload'
reopened=cmd('file.open',data=base64.b64encode((ROOT/'design/FPML.figcraft').read_bytes()).decode(),name='FPML-reopened.figcraft')
reopened_doc=tree()
assert len([v for v in walk(reopened_doc) if v.get('interactions')])>=10
assert 'Save as current team' in json.dumps(reopened_doc)
verification=dict(reopened=reopened,prototypeLinksPersisted=len(links),componentOverridePersisted=True,
 missingFonts=cmd('text.missingFonts'),document=rpc('document.inspect',dict(depth=1,allPages=True)),
 playback='Not verified: window 0 is minimised or hidden; ui.screenshot needs it on screen. Native ui.render works.')
(ROOT/'design/verification.json').write_text(json.dumps(verification,indent=2))
print('Saved native design and 8 exports.')
