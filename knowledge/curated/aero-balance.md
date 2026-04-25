---
title: "Aero Balance"
description: "Notes on aerodynamic balance and its effects on handling and setup decisions."
tags: [aero, balance, setup]
created: "2026-04-25"
source: "moved from root"
---

# Aero Balance

## Purpose
This document introduces aero balance in generic terms for a race engineering workflow. It focuses on how front and rear aerodynamic load influence vehicle balance and driver confidence.

## What Aero Balance Means
Aero balance describes how total aerodynamic load is distributed between the front and rear of the car. Even if total downforce is high, the car can still feel poor if the front-rear distribution is wrong.

A stable car usually needs:

- Enough front load to support turn-in and high-speed direction change.
- Enough rear load to support braking stability, traction confidence, and sustained cornering.

The right split depends on the car concept, tire behavior, and track speed profile.

## Downforce and Drag
Aerodynamic devices can increase downforce, drag, or both. More downforce often improves cornering and braking support, but extra drag may reduce top speed and acceleration.

This creates a trade-off:

- More wing generally improves stability and grip in medium and high-speed corners.
- Less wing generally improves straight-line speed but may reduce confidence and consistency.

The fastest package over a lap is not always the lowest-drag package.

## Front vs Rear Aero Load
Very general tendencies:

- More front aero load can improve turn-in and reduce high-speed understeer.
- Too much front aero load can make the rear feel nervous, especially in fast entries.
- More rear aero load can improve rear stability and traction confidence.
- Too much rear aero bias can make the car reluctant to rotate.

Aero balance should therefore be judged by phase and speed range, not by a single overall feeling.

## Ride Height and Rake
Aero performance is highly sensitive to ride height. As speed rises, the car compresses under aero load, and this changes the airflow under and around the body.

Rake refers to the difference between rear and front ride height. Depending on the car concept, rake can influence front downforce generation, diffuser behavior, and overall sensitivity.

This means aero setup cannot be separated from suspension setup. Springs, dampers, bump stops, and platform control all affect how the aero map behaves in motion.

## Typical Setup Levers
Common aerodynamic levers include:

- Rear wing angle.
- Front splitter or flap angle.
- Ride heights.
- Rake.
- Bodywork or duct configuration where applicable.

Generic tendencies:

- More rear wing: more rear downforce, more drag, more high-speed security.
- More front flap or splitter effect: more front bite, stronger turn-in response, possible rear instability if overdone.
- Lower ride heights: often more downforce up to a point, with possible sensitivity or stall risk depending on the platform.

## Diagnostic Patterns
Examples of likely aero-related issues:

- Stable in slow corners but understeers in fast corners: possible lack of front aero support.
- Stable on entry but unstable in fast direction change: possible rear aero weakness or platform instability.
- Good one lap, inconsistent over bumps or fuel change: possible aero sensitivity to ride height variation.

These are clues, not proof. Mechanical balance and tire pressures must still be checked.

## Testing Approach
A practical approach:

1. Separate low-speed and high-speed complaints.
2. Hold tire pressures and fuel conditions as constant as possible.
3. Change one aero lever at a time.
4. Monitor lap-time trend, driver confidence, and straight-line penalty together.
5. Re-check ride heights after meaningful aero changes.

The most useful result is often not the strongest peak grip, but the setup that gives the driver repeatable confidence in fast corners.

## Practical Note
For a v0 RAG system, aero balance should be framed in simple cause-and-effect language. The assistant only needs to know that aerodynamic load changes grip distribution with speed, that platform control matters, and that aero decisions must be evaluated against drag and stability together.
