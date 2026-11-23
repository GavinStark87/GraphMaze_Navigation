#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Graph Maze Navigation Task -- MAIN TASK
MenoMaps Project - UC Irvine Spatial Neuroscience Lab

Run after GraphMaze_Practice.py has been completed.
4 runs total: 2 brick + 2 hedge, 40 trials each, 160 trials total.
Environment start order (brick vs hedge first) is randomized, AND the
order of each environment's two 40-trial runs is independently randomized.
Each environment's two runs always stay adjacent to one another.
No practice, no feedback. Trial type shown as a short centered label
("path" / "straight-line") between the cue image and the two choice images.
Env label screens show the maze reference image, matching the practice format.
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os, sys
import random as pyrandom
from psychopy.hardware import keyboard

# -- Paths -------------------------------------------------------------------
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

data_dir = os.path.join(_thisDir, 'data')
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)

# -- Experiment Info ---------------------------------------------------------
psychopyVersion = '2021.2.3'
expName = 'GraphMaze_Navigation'
expInfo = {'Participant ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (
    expInfo['Participant ID'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_thisDir,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename + '.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)

endExpNow = False
frameTolerance = 0.001

# ===========================================================================
# ENVIRONMENT PRESENTATION ORDER
# ===========================================================================
# Set FORCED_START_ENV to 'brick' or 'hedge' to manually control which
# environment runs first. Set to None to randomize automatically.
FORCED_START_ENV = None   # 'brick', 'hedge', or None for random

if FORCED_START_ENV in ('brick', 'hedge'):
    env_order = [FORCED_START_ENV, 'hedge' if FORCED_START_ENV == 'brick' else 'brick']
else:
    env_order = ['brick', 'hedge']
    pyrandom.shuffle(env_order)

thisExp.addData('env_order', '_'.join(env_order))
thisExp.addData('env_1_first', env_order[0])
thisExp.addData('env_2_second', env_order[1])
thisExp.nextEntry()

# -- Window ------------------------------------------------------------------
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] is not None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()

# -- Colors ------------------------------------------------------------------
COLOR_BLACK = [0, 0, 0]
COLOR_BLUE  = [0.2, 0.55, 0.95]     # lighter blue -- path distance trials
COLOR_PEACH = [0.914, 0.506, 0.090] # peach        -- straight-line trials

# -- Ready slide text --------------------------------------------------------
SLIDE_READY_BODY = (
    "You will now begin the main task. \n\n"
    "The task is split into 4 runs of 40 trials each, covering the two "
    "environments you have learned.\n\n"
    "You will have 10 seconds to respond to each trial. "
    "You will not be given feedback on your performance.\n\n"
    "During each trial, a label between the images will tell you whether to judge "
    "path distance (blue) or straight-line distance (peach) to the top object -- "
    "they may not be the same answer!\n\n"
    "Do you have any questions?"
)

# -- Global Timers -----------------------------------------------------------
globalClock = core.Clock()
routineTimer = core.CountdownTimer()

# ===========================================================================
# VISUAL COMPONENTS
# ===========================================================================

# Fixation cross
fixClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+', font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)

# Environment label + maze reference image (matches practice format exactly)
envClock = core.Clock()
env_label = visual.TextStim(win=win, name='env_label',
    text='', font='Arial',
    pos=(0, 0.43), height=0.048, wrapWidth=1.4, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)
env_advance = visual.TextStim(win=win, name='env_advance',
    text='Press 5 to continue.',
    font='Arial', pos=(0, -0.46), height=0.038, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=-1.0)
env_maze_image = visual.ImageStim(
    win=win, name='env_maze_image',
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.06), size=(0.72, 0.72),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Trial components (black text on colored backgrounds)
trialClock = core.Clock()

# Centered distance-type label -- replaces the full question sentence.
# Sits between the cue image (top) and the left/right choice images (bottom).
trial_type_label = visual.TextStim(win=win, name='trial_type_label',
    text='', font='Arial',
    pos=(0, -0.07), height=0.05, wrapWidth=0.8, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=0.0, bold=True)

cue_image = visual.ImageStim(
    win=win, name='cue_image',
    image='sin', mask=None,
    ori=0, pos=(0, 0.12), size=(0.25, 0.25),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

cue_label_stim = visual.TextStim(win=win, name='cue_label_stim',
    text='', font='Arial',
    pos=(0, -0.02), height=0.042, wrapWidth=0.5, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=-2.0)

left_image = visual.ImageStim(
    win=win, name='left_image',
    image='sin', mask=None,
    ori=0, pos=(-0.22, -0.22), size=(0.22, 0.22),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)

left_label_stim = visual.TextStim(win=win, name='left_label_stim',
    text='', font='Arial',
    pos=(-0.22, -0.36), height=0.042, wrapWidth=0.35, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=-4.0)

right_image = visual.ImageStim(
    win=win, name='right_image',
    image='sin', mask=None,
    ori=0, pos=(0.22, -0.22), size=(0.22, 0.22),
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)

right_label_stim = visual.TextStim(win=win, name='right_label_stim',
    text='', font='Arial',
    pos=(0.22, -0.36), height=0.042, wrapWidth=0.35, ori=0,
    color='black', colorSpace='rgb', opacity=1, depth=-6.0)

trial_resp = keyboard.Keyboard()

# End screen
endClock = core.Clock()
thankyou = visual.TextStim(win=win, name='thankyou',
    text='You have now completed the experiment.\n\nThank you for your participation!',
    font='Arial', pos=(0, 0.1), height=0.06, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=0.0)
finalslide = visual.TextStim(win=win, name='finalslide',
    text='Press 5 to exit.',
    font='Arial', pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1, depth=-1.0)
final_key = keyboard.Keyboard()

# ===========================================================================
# HELPER FUNCTIONS
# ===========================================================================

def load_conditions(csv_path):
    """Load a conditions CSV, quitting with a clear message if not found."""
    if not os.path.isfile(csv_path):
        print('ERROR: conditions file not found: ' + csv_path)
        print('Expected location: ' + os.path.join(_thisDir, csv_path))
        win.close()
        core.quit()
    try:
        return data.importConditions(csv_path)
    except Exception as e:
        print('ERROR: failed to read ' + csv_path)
        print(str(e))
        win.close()
        core.quit()


def build_env_runs(conditions_list, n_runs=2, trials_per_run=40):
    """
    Shuffle a full condition list, split it into n_runs equal chunks,
    then shuffle the ORDER of the chunks themselves. This means which
    40-trial half ends up being labeled "Run 1" vs "Run 2" is randomized,
    satisfying the "Randomized run order" requirement per environment.
    """
    shuffled = list(conditions_list)
    pyrandom.shuffle(shuffled)
    total_needed = n_runs * trials_per_run
    if len(shuffled) < total_needed:
        print('WARNING: only {} trials available, need {} for {} runs of {}'.format(
            len(shuffled), total_needed, n_runs, trials_per_run))
    chunks = []
    for i in range(n_runs):
        start = i * trials_per_run
        end = start + trials_per_run
        chunks.append(shuffled[start:end])
    pyrandom.shuffle(chunks)   # randomize which chunk is presented first
    return chunks


def show_fixation(duration=1.0):
    """Display fixation cross for a fixed duration on black background."""
    win.color = COLOR_BLACK
    routineTimer.reset()
    routineTimer.add(duration)
    fixation.status = NOT_STARTED
    fixation.tStart = None
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    fixClock.reset(-_timeToFirstFrame)
    frameN = -1
    while routineTimer.getTime() > 0:
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            fixation.frameNStart = frameN
            fixation.tStart = fixClock.getTime()
            fixation.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(fixation, 'tStartRefresh')
            fixation.setAutoDraw(True)
        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        win.flip()
    fixation.setAutoDraw(False)
    routineTimer.reset()


def show_text_slide(body_text):
    """Display a text-only slide on a black background. Key 5 to advance."""
    win.color = COLOR_BLACK
    slideClock = core.Clock()

    body_stim = visual.TextStim(win,
        text=body_text, font='Arial',
        pos=(0, 0.08), height=0.036,
        wrapWidth=1.5, color='white', colorSpace='rgb',
        depth=-1.0)
    advance_stim = visual.TextStim(win,
        text='Press 5 to continue.',
        font='Arial', pos=(0, -0.47), height=0.031,
        color=[0.4, 0.4, 0.4], colorSpace='rgb', depth=-2.0)
    vis_comps = [body_stim, advance_stim]

    slide_resp = keyboard.Keyboard()
    for comp in vis_comps:
        comp.status = NOT_STARTED
        comp.tStart = None
    slide_resp.status = NOT_STARTED
    slide_resp.keys = []
    _allKeys = []
    continueRoutine = True
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    slideClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        tThisFlip = win.getFutureFlipTime(clock=slideClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        for comp in vis_comps:
            if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                comp.frameNStart = frameN
                comp.tStart = slideClock.getTime()
                comp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(comp, 'tStartRefresh')
                comp.setAutoDraw(True)
        waitOnFlip = False
        if slide_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            slide_resp.frameNStart = frameN
            slide_resp.tStart = slideClock.getTime()
            slide_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(slide_resp, 'tStartRefresh')
            slide_resp.status = STARTED
            waitOnFlip = True
            win.callOnFlip(slide_resp.clock.reset)
            win.callOnFlip(slide_resp.clearEvents, eventType='keyboard')
        if slide_resp.status == STARTED and not waitOnFlip:
            theseKeys = slide_resp.getKeys(keyList=['5'], waitRelease=False)
            _allKeys.extend(theseKeys)
            if len(_allKeys):
                continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        if continueRoutine:
            win.flip()

    for comp in vis_comps:
        comp.setAutoDraw(False)
    routineTimer.reset()


def show_env_label(label_text, maze_path=None):
    """
    Display environment name + title, same format as the practice maze
    screen. Shows the maze reference image below the title if provided.
    Key 5 to advance.
    """
    win.color = COLOR_BLACK
    env_label.setText(label_text)

    display_comps = [env_label, env_advance]
    if maze_path:
        env_maze_image.setImage(maze_path)
        display_comps = [env_label, env_maze_image, env_advance]

    env_resp = keyboard.Keyboard()
    for comp in display_comps:
        comp.status = NOT_STARTED
        comp.tStart = None
    env_resp.status = NOT_STARTED
    env_resp.keys = []
    _allKeys = []
    continueRoutine = True
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    envClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        tThisFlip = win.getFutureFlipTime(clock=envClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        for comp in display_comps:
            if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                comp.frameNStart = frameN
                comp.tStart = envClock.getTime()
                comp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(comp, 'tStartRefresh')
                comp.setAutoDraw(True)
        waitOnFlip = False
        if env_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            env_resp.frameNStart = frameN
            env_resp.tStart = envClock.getTime()
            env_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(env_resp, 'tStartRefresh')
            env_resp.status = STARTED
            waitOnFlip = True
            win.callOnFlip(env_resp.clock.reset)
            win.callOnFlip(env_resp.clearEvents, eventType='keyboard')
        if env_resp.status == STARTED and not waitOnFlip:
            theseKeys = env_resp.getKeys(keyList=['5'], waitRelease=False)
            _allKeys.extend(theseKeys)
            if len(_allKeys):
                continueRoutine = False
        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        if continueRoutine:
            win.flip()

    for comp in display_comps:
        comp.setAutoDraw(False)
    routineTimer.reset()


def run_trial(trialData):
    """
    Run one main trial (no feedback). Returns (keys, rt, corr).
    Background: blue for route, peach for line.
    trial_type_label shows 'path' or 'straight-line' centered between images.
    Key map: 1 = left, 2 = right. 10-second response window.
    """
    trial_type = trialData['trial_type']
    win.color = COLOR_BLUE if trial_type == 'route' else COLOR_PEACH

    cue_image.setImage(trialData['cueImage'])
    left_image.setImage(trialData['leftImage'])
    right_image.setImage(trialData['rightImage'])
    cue_label_stim.setText(trialData['cueLabel'])
    left_label_stim.setText(trialData['leftLabel'])
    right_label_stim.setText(trialData['rightLabel'])
    trial_type_label.setText('path' if trial_type == 'route' else 'straight-line')

    trial_resp.keys = []
    trial_resp.rt = []
    _trial_allKeys = []

    vis_comps = [trial_type_label, cue_image, cue_label_stim,
                 left_image, left_label_stim,
                 right_image, right_label_stim]
    for comp in vis_comps + [trial_resp]:
        comp.tStart = None
        comp.tStop = None
        comp.tStartRefresh = None
        comp.tStopRefresh = None
        if hasattr(comp, 'status'):
            comp.status = NOT_STARTED

    trialCountdown = core.CountdownTimer(10)

    continueRoutine = True
    _timeToFirstFrame = win.getFutureFlipTime(clock='now')
    trialClock.reset(-_timeToFirstFrame)
    frameN = -1

    while continueRoutine:
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        for comp in vis_comps:
            if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
                comp.frameNStart = frameN
                comp.tStart = trialClock.getTime()
                comp.tStartRefresh = tThisFlipGlobal
                win.timeOnFlip(comp, 'tStartRefresh')
                comp.setAutoDraw(True)

        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            trial_resp.frameNStart = frameN
            trial_resp.tStart = trialClock.getTime()
            trial_resp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(trial_resp, 'tStartRefresh')
            trial_resp.status = STARTED
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')

        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['1', '2'], waitRelease=False)
            _trial_allKeys.extend(theseKeys)
            if len(_trial_allKeys):
                trial_resp.keys = _trial_allKeys[0].name
                trial_resp.rt   = _trial_allKeys[0].rt
                key_map = {'1': 'left', '2': 'right'}
                response_dir = key_map.get(trial_resp.keys, trial_resp.keys)
                if (response_dir == str(trialData['corrAns']) or
                        response_dir == trialData['corrAns']):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                continueRoutine = False

        if trialCountdown.getTime() <= 0:
            continueRoutine = False

        if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
            core.quit()
        if continueRoutine:
            win.flip()

    for comp in vis_comps:
        comp.setAutoDraw(False)

    if trial_resp.keys in ['', [], None]:
        trial_resp.keys = None
        trial_resp.rt   = None
        trial_resp.corr = 0

    win.color = COLOR_BLACK
    return trial_resp.keys, trial_resp.rt, trial_resp.corr


# ===========================================================================
# EXPERIMENT FLOW
# ===========================================================================

RUNS_PER_ENV = 2
TRIALS_PER_RUN = 40

env_configs = {
    'brick': {
        'label': 'Brick Maze',
        'conditions_file': 'nav_task_conditions_brick.csv',
        'maze_image': 'stimuli/brick_maze.png',
    },
    'hedge': {
        'label': 'Hedge Maze',
        'conditions_file': 'nav_task_conditions.csv',
        'maze_image': 'stimuli/hedge_maze.png',
    }
}

# -- Build run chunks for each environment. Chunk order (which half is
#    Run 1 vs Run 2) is randomized independently for each environment. -----
env_run_conditions = {}
for env_name in env_order:
    cfg = env_configs[env_name]
    full_conditions = load_conditions(cfg['conditions_file'])
    env_run_conditions[env_name] = build_env_runs(
        full_conditions, RUNS_PER_ENV, TRIALS_PER_RUN)

# -- Fixed run sequence: each env's two runs stay adjacent, in the order
#    env_order already decided above. ----------------------------------------
run_sequence = []
for env_name in env_order:
    for run_idx in range(1, RUNS_PER_ENV + 1):
        run_sequence.append((env_name, run_idx))

thisExp.addData('run_sequence', '_'.join(
    ['{}Run{}'.format(e, r) for e, r in run_sequence]))
thisExp.nextEntry()

# 1. Ready slide
show_text_slide(SLIDE_READY_BODY)

trial_handlers = {}
total_runs = len(run_sequence)
run_counter = 0

for env_name, run_idx in run_sequence:
    run_counter += 1
    cfg = env_configs[env_name]
    run_conditions = env_run_conditions[env_name][run_idx - 1]

    show_env_label(
        '{} (Run {} of {})'.format(cfg['label'], run_idx, RUNS_PER_ENV),
        maze_path=cfg['maze_image'])

    handler_key = '{}_run{}'.format(env_name, run_idx)
    trials = data.TrialHandler(nReps=1, method='sequential',
        extraInfo=expInfo, originPath=-1,
        trialList=run_conditions,
        seed=None, name=handler_key)
    thisExp.addLoop(trials)
    trial_handlers[handler_key] = trials

    for thisTrial in trials:
        currentLoop = trials
        if thisTrial is not None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))

        show_fixation(1.0)
        respKeys, respRT, respCorr = run_trial(thisTrial)

        trials.addData('trial_resp.keys', respKeys)
        trials.addData('trial_resp.corr', respCorr)
        if respKeys is not None:
            trials.addData('trial_resp.rt', respRT)
        trials.addData('trial_type', thisTrial['trial_type'])
        trials.addData('cue_image.file', thisTrial['cueImage'])
        trials.addData('left_image.file', thisTrial['leftImage'])
        trials.addData('right_image.file', thisTrial['rightImage'])
        trials.addData('env_name', env_name)
        trials.addData('run_number', run_idx)
        trials.addData('global_run_index', run_counter)

        routineTimer.reset()
        thisExp.nextEntry()

    event.clearEvents()
    defaultKeyboard.clearEvents()

    if run_counter < total_runs:
        show_text_slide(
            'You have completed Run {} of {}.\n\n'
            'Press 5 when you are ready to begin the next run.'.format(
                run_counter, total_runs))

# -- Save per-run trial files -------------------------------------------------
for handler_key, trials in trial_handlers.items():
    if trials.trialList not in ([], [None], None):
        params = trials.trialList[0].keys()
    else:
        params = []
    trials.saveAsText(filename + '_' + handler_key + '_trials.csv', delim=',',
        stimOut=params,
        dataOut=['n', 'all_mean', 'all_std', 'all_raw'])

# ===========================================================================
# END SCREEN
# ===========================================================================
win.color = COLOR_BLACK
continueRoutine = True
final_key.keys = []
final_key.rt = []
_final_allKeys = []

endComponents = [thankyou, final_key, finalslide]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
_timeToFirstFrame = win.getFutureFlipTime(clock='now')
endClock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine:
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    for comp in [thankyou, finalslide]:
        if comp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            comp.frameNStart = frameN
            comp.tStart = endClock.getTime()
            comp.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(comp, 'tStartRefresh')
            comp.setAutoDraw(True)
    waitOnFlip = False
    if final_key.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        final_key.frameNStart = frameN
        final_key.tStart = endClock.getTime()
        final_key.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(final_key, 'tStartRefresh')
        final_key.status = STARTED
        waitOnFlip = True
        win.callOnFlip(final_key.clock.reset)
        win.callOnFlip(final_key.clearEvents, eventType='keyboard')
    if final_key.status == STARTED and not waitOnFlip:
        theseKeys = final_key.getKeys(keyList=['5'], waitRelease=False)
        _final_allKeys.extend(theseKeys)
        if len(_final_allKeys):
            final_key.keys = _final_allKeys[-1].name
            final_key.rt   = _final_allKeys[-1].rt
            continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=['escape']):
        core.quit()
    if continueRoutine:
        win.flip()

for comp in [thankyou, finalslide]:
    comp.setAutoDraw(False)
if final_key.keys in ['', [], None]:
    final_key.keys = None
thisExp.addData('final.keys', final_key.keys)
if final_key.keys is not None:
    thisExp.addData('final.rt', final_key.rt)
thisExp.nextEntry()
routineTimer.reset()

# -- Wrap up -----------------------------------------------------------------
win.flip()
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()