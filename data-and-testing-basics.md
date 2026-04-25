# Data and Testing Basics

## Purpose
This document defines a simple, repeatable testing workflow for setup development. It is written for a generic sim racing race engineer workflow where controlled iteration matters more than collecting large amounts of noisy data.

## Why Testing Discipline Matters
Setup work becomes unreliable when too many variables change at once. A faster lap does not automatically prove that a setup change was better, because fuel, traffic, tire state, track evolution, and driver input can all distort the result.

The goal of testing is not only to find speed. The goal is to understand cause and effect.

## Single-Variable Testing
The most reliable basic method is single-variable testing.

That means:

- Start from a known baseline.
- Change one meaningful parameter.
- Repeat the run in similar conditions.
- Compare the result using both lap time and behavior.

If several parameters change at once, it becomes difficult to know which one created the observed effect.

## What to Record
A useful test log should capture both objective and subjective information.

Suggested fields:

- Track and layout.
- Car and baseline setup name.
- Weather and track condition.
- Fuel load.
- Tire compound.
- Cold and hot pressures.
- Key setup changes.
- Best lap and average representative laps.
- Driver comments by corner phase.
- Notes on confidence, curb behavior, braking, and traction.

Even a small but consistent dataset becomes valuable if it is structured well.

## Reading Results
A strong setup change usually shows up in more than one way:

- Improved repeatability across multiple laps.
- Better confidence in the problem corners.
- More stable tire behavior.
- Less correction needed from the driver.
- Competitive lap time without a major downside elsewhere.

A setup that gains a small peak but becomes hard to drive may be worse over a race run.

## Common Mistakes
Frequent testing mistakes include:

- Judging from one hero lap.
- Changing multiple variables together.
- Comparing runs with very different fuel loads.
- Ignoring tire warm-up state.
- Mixing low-speed and high-speed complaints into one diagnosis.
- Forgetting to write down exactly what changed.

These mistakes create false confidence and make future setup work harder.

## Driver Feedback Integration
Driver comments should be logged in a structured way. Free-form notes are useful, but they become more useful when linked to corner phase and speed type.

Examples:

- Entry instability under trail braking.
- Mid-corner push in long loaded turns.
- Exit wheelspin in second gear.
- Poor curb compliance in chicanes.

This kind of phrasing helps connect subjective feedback to likely setup domains such as tires, dampers, roll balance, or aero.

## Minimal v0 Workflow
A practical v0 workflow:

1. Build one stable baseline setup.
2. Identify the biggest limitation over a representative lap.
3. Choose one setup lever that should affect that limitation.
4. Run a short controlled test.
5. Log both numbers and comments.
6. Keep, revert, or refine the change.

This process is simple, but it scales well into more advanced telemetry and RAG-based recommendation systems.

## Practical Note
For a first RAG loop, structured testing knowledge is as important as setup theory. A race engineer assistant becomes more useful when it can tell the difference between a true setup trend and a noisy observation.
