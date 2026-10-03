# Graph Maze Navigation Task
### MenoMaps Project — UC Irvine Spatial Neuroscience Lab

**Author:** Gavin Stark
**Contact:** gestark@uci.edu
**Last updated:** 10/2/2026

---

## Overview

The Graph Maze Navigation Task is a PsychoPy experiment in which
participants are shown objects from spatial environments they have
previously learned and asked to judge relative distances between
them. On each trial a cue object is presented at the top of the
screen alongside two choice objects. Participants indicate which
choice object is closer to the cue via one of two distance types:

- **Path / route distance** — shortest distance if constrained to
  the navigable paths of the environment (blue background)
- **Straight-line distance** — shortest Euclidean distance if
  walking in a straight line (peach background)

The task is delivered as a single Python script (no Builder
.psyexp file) and is designed for use with a button box or
keyboard using number keys only (1 = left, 2 = right).

> **Origin:** This script was developed from scratch for the
> MenoMaps project, using the UC Irvine Spatial Neuroscience Lab's
> Paper Folding Task (Alina Tu, 2022) as a structural and
> coding-style reference point. No Paper Folding stimuli, condition
> files, or instruction content are used in this task.

---

## Environments & Stimuli

The task covers two spatial environments, each with its own
practice block followed by a randomised main trial block.

### Brick Maze (24 main trials)
12 objects, each serving as a cue once per distance type.
Distances derived from Brick_maze_distances.csv.

| Object        | Image file                  |
|---------------|-----------------------------|
| Chair         | brick_chair.png             |
| Mailbox       | brick_mailbox.png           |
| Telescope     | brick_telescope.png         |
| Plant         | brick_plant.png             |
| Oven          | brick_oven.png              |
| Trash Can     | brick_trashcan.png          |
| Picnic Table  | brick_picnicTable.png       |
| Harp          | brick_harp.png              |
| Well          | brick_well.png              |
| Wheelbarrow   | brick_wheelbarrow.png       |
| Bookshelf     | brick_bookshelf.png         |
| Piano         | brick_piano.png             |

### Hedge Maze (16 main trials)
8 objects, each serving as a cue once per distance type.

| Object        | Image file                  |
|---------------|-----------------------------|
| Chair         | maze_chair.png              |
| Clock         | maze_clock.png              |
| Compass       | maze_compass.png            |
| Guitar        | maze_guitar.png             |
| Lamp Post     | maze_lampPost.png           |
| Snowman       | maze_snowman.png            |
| Space Shuttle | maze_spaceShuttle.png       |
| Umbrella      | maze_umbrella.png           |

All images live in the stimuli/ subfolder alongside the script.

---

## Folder Structure

```
GraphMaze_Navigation/
├── GraphMaze_Navigation.py          # Main experiment script
├── nav_task_practice_fruit.csv      # Fruit practice (4 trials)
├── nav_task_practice_brick.csv      # Brick practice (2 trials)
├── nav_task_practice_hedge.csv      # Hedge practice (2 trials)
├── nav_task_conditions_brick.csv    # Brick main trials (24)
├── nav_task_conditions.csv          # Hedge main trials (16)
├── stimuli/
│   ├── prac_maze.png                # Fruit practice maze image
│   ├── brick_maze.png               # Brick environment screenshot
│   ├── hedge_maze.png               # Hedge environment screenshot
│   ├── prac_apple.png
│   ├── prac_orange.png
│   ├── prac_banana.png
│   ├── prac_grape.png
│   ├── brick_chair.png
│   ├── ... (all brick object images)
│   ├── maze_chair.png
│   └── ... (all hedge object images)
├── data/                            # Auto-created at runtime
│   └── (participant output files — excluded from version control)
├── README.md
└── .gitignore
```

---

## Task Flow

1. Instruction slide (text, no PNG required)
   — color legend for blue / peach backgrounds shown here
2. Fruit practice maze image displayed
3. Fruit practice block — 4 trials with feedback (sequential)
4. Pre-task instruction slide
5. Brick maze environment label + maze image
6. Brick practice block — 2 trials with feedback (sequential)
7. Brick main trials — 24 trials, no feedback (randomised)
8. Hedge maze environment label + maze image
9. Hedge practice block — 2 trials with feedback (sequential)
10. Hedge main trials — 16 trials, no feedback (randomised)
11. End screen

**Total main trials: 40 (24 brick + 16 hedge)**
**Response window: 10 seconds per trial**
No-response trials are recorded as keys=None, rt=None, corr=0.

---

## Response Keys

| Key              | Meaning                          |
|------------------|----------------------------------|
| 1                | Left choice object               |
| 2                | Right choice object              |
| Any number (0–9) | Advance slide / continue         |
| Esc              | Quit experiment at any time      |

---

## Condition File Format

All six CSV files share the same column schema:

```
cueImage, leftImage, rightImage, corrAns, trial_type,
cueLabel, leftLabel, rightLabel, corrLabel
```

- corrAns: "left" or "right"
- trial_type: "route" or "line"
- Image paths are relative to the script directory
  (e.g. stimuli/brick_chair.png)

---

## Distance Matrix Convention

Distances were derived from environment-specific CSV files
(e.g. Brick_maze_distances.csv):

- **Upper triangle** (row index < col index) = straight-line distance
- **Lower triangle** (row index > col index) = route/path distance

Correct answers in the condition files were verified against this
matrix before piloting. Re-verify if any object positions change.

---

## Setup & Running

1. Install PsychoPy 2021.2.3 or later.
2. Place all stimuli images in the stimuli/ subfolder.
3. Ensure all six CSV condition files are in the same folder as
   the script.
4. Run GraphMaze_Navigation.py from the PsychoPy runner or
   directly via Python.
5. Enter a Participant ID in the dialog box.
6. The data/ folder will be created automatically on first run.

Output files saved to data/:
- `<ID>_GraphMaze_Navigation_<date>.csv`  (wide-format trial data)
- `<ID>_GraphMaze_Navigation_<date>.psydat`
- `<ID>_GraphMaze_Navigation_<date>.log`
- `<ID>_GraphMaze_Navigation_<date>brick_trials.csv`
- `<ID>_GraphMaze_Navigation_<date>hedge_trials.csv`

---

## Version History

### Version 1.0 Beta — 10/2/2026
Initial working version. Not yet signed off for data collection.

- Native text-based instruction slides; no PNG slide images needed.
  Edit SLIDE1_BODY and SLIDE2_BODY at the top of the script to
  update instructions without touching any other code.
- Number-key-only input: 1 = left, 2 = right, any number = advance.
  Spacebar not used anywhere.
- Blue background (COLOR_BLUE) for route/path trials; peach
  (COLOR_PEACH) for straight-line trials. Color legend shown on
  first instruction slide.
- 10-second response timer via core.CountdownTimer(10).
- Fixed _trial_allKeys bug: theseKeys was never appended to
  _trial_allKeys before reading _trial_allKeys[0], causing an
  IndexError crash on the first practice trial.
- event.clearEvents() + defaultKeyboard.clearEvents() added after
  each practice block to prevent stale key presses from immediately
  ending the first main trial (post-practice crash fix).
- env_label and maze_title_stim positions centered at x=0, y=0.43
  to prevent top-left screen clipping.
- env_maze_image ImageStim added; show_env_label() accepts optional
  maze_path so brick_maze.png and hedge_maze.png display on their
  environment label screens.
- env_advance prompt added to show_practice_maze() and repositioned
  to y=-0.46 on all maze screens so it clears the image.
- Lighter blue background: COLOR_BLUE changed from dark steel
  [-0.286, 0.216, 0.671] to sky blue [0.2, 0.55, 0.95].
- Green feedback elements set to deep forest green [0, 0.32, 0]
  for readability against both trial background colors.
- Practice maze image size set to (0.75, 0.75) for screen fit.
- load_conditions() wrapped in try/except; thisExp.abort() removed
  from error path to prevent double-crash on bad CSV files.
- data/ directory auto-created at startup if not present.
- Adapted from the UC Irvine Spatial Neuroscience Lab Paper Folding
  Task (Alina Tu, 2022) as a coding-style starting point.