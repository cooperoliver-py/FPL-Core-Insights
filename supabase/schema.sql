-- Apply once in Supabase SQL Editor. Only the server writes private state.
create table if not exists public.fpml_state (
  owner_id uuid not null references auth.users(id),
  key text not null,
  value jsonb not null,
  primary key (owner_id, key)
);
alter table public.fpml_state enable row level security;
revoke all on public.fpml_state from anon, authenticated;
create or replace function public.fpml_save_team(owner uuid, expected_revision integer, payload jsonb)
returns boolean language plpgsql security definer set search_path = public as $$
declare current_revision integer;
begin
  perform pg_advisory_xact_lock(hashtext(owner::text));
  select (value->'team'->>'revision')::integer into current_revision
    from fpml_state where owner_id = owner and key = 'team';
  if coalesce(current_revision, 0) <> expected_revision then return false; end if;
  insert into fpml_state(owner_id, key, value) values (owner, 'team', payload)
    on conflict (owner_id, key) do update set value = excluded.value;
  return true;
end;
$$;
revoke all on function public.fpml_save_team(uuid, integer, jsonb) from public, anon, authenticated;
grant execute on function public.fpml_save_team(uuid, integer, jsonb) to service_role;
