---
name: FPML
description: A restrained personal workspace for FPL decisions.
colors:
  bg: "#101417"
  panel: "#181e22"
  line: "#2d363d"
  text: "#f4f7f5"
  muted: "#a6b2b9"
  green: "#77c99b"
typography:
  body:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: "16px"
    fontWeight: 400
  headline:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 500
rounded:
  control: "6px"
components:
  button-primary:
    backgroundColor: "{colors.text}"
    textColor: "{colors.bg}"
    rounded: "{rounded.control}"
    padding: "11px 18px"
---

## Overview

FPML is a compact working interface. Its identity comes from aligned squad rows, quiet separators, strong numbers and a narrow decision column. The rendered application in `frontend/src/styles.css` is the implementation reference; `design/FPML.figcraft` captures the editable composition studies.

## Colors

Dark neutral surfaces support extended review. White identifies primary actions and current selections. Muted text carries secondary context. Green highlights positive gain and successful state, with words or symbols conveying the same meaning.

## Typography

Self-hosted IBM Plex Sans uses regular, medium and semibold weights. Tabular numerals keep prices and points aligned. Sentence case is the default. Large numbers convey the decision; detailed evidence stays in disclosures and player sheets.

## Layout

Desktop Team pairs a flexible squad column with a decision column of 300–360px. Below 768px, the decision appears before the long squad list and navigation moves to the bottom. Layouts also adapt at 1024px and 1191px. Content begins at a 320px minimum width. Mobile sheets use dynamic viewport height and safe-area padding.

## Elevation & Depth

Separators and surface tones establish hierarchy. Native modal dialogs provide focus containment and a dimmed backdrop. Avoid adding floating containers around every metric.

## Shapes

Controls have gently rounded corners. Rows remain flat and aligned. Round badges indicate player roles, rather than enclosing ordinary content.

## Components

Primary actions have a 44px minimum height and restrained press feedback. Native inputs retain labels and browser validation. Visible keyboard focus uses an offset white outline. Forecast strips align the available Gameweeks. Native disclosures reveal calculation meaning and supporting tables. Player details and the team editor use native dialogs with explicit close buttons. Disabled actions remain visually distinct. Reduced-motion preferences remove transitions.

## Do's and Don'ts

- Do preserve units, missing-value distinctions and the meaning of weighted gain.
- Do keep the latest calculated result visible while a draft needs recalculation.
- Do use the same core tasks on desktop and mobile.
- Don't use a football pitch, decorative imagery or repetitive card grids.
- Don't replace useful labels with unexplained icons or colour alone.
