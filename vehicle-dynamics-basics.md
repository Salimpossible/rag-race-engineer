# Vehicle Dynamics Basics

## Purpose
This document introduces the core ideas behind vehicle dynamics for a generic racing car. It focuses on concepts that are useful in setup work and race engineering without depending on a specific simulator, series, or car.

## Core Axes of Motion
A car moves and reacts in three main axes:

- Longitudinal: acceleration and braking.
- Lateral: cornering and direction changes.
- Vertical: bumps, curbs, heave, pitch, and roll.

These motions happen together. A setup change that improves one area can influence the others, which is why setup work should be treated as a system rather than a list of independent parts.

## Tire Force Basics
Tires generate the forces that allow the car to brake, turn, and accelerate. The vehicle only changes direction or speed because the contact patches interact with the road surface.

Important terms:

- Slip angle: the difference between the direction a wheel points and the direction it actually travels.
- Slip ratio: the difference between wheel rotational speed and actual road speed during braking or acceleration.
- Contact patch: the small area where the tire touches the track.
- Grip: the tire's ability to generate force before sliding.

In practice, setup changes often work by changing how efficiently each tire uses its available grip.

## Load Transfer
Load transfer is one of the most important concepts in setup work. When the car accelerates, brakes, or corners, load shifts between tires.

There are three useful categories:

- Longitudinal load transfer: front-to-rear movement during braking and acceleration.
- Lateral load transfer: side-to-side movement during cornering.
- Vertical load variation: changes caused by bumps, crests, curbs, and aerodynamic load.

Under braking, the front tires usually gain load and the rear tires lose load. Under acceleration, the opposite happens. In cornering, the outside tires usually gain load and the inside tires lose load.

More load on a tire does not produce grip in a perfectly linear way. Because of tire load sensitivity, doubling the load does not double the available grip. This is a major reason why controlling load transfer distribution matters for balance.

## Pitch, Roll, and Heave
The body can move in three main ways relative to the suspension:

- Pitch: nose up or nose down rotation.
- Roll: body leaning to one side in a corner.
- Heave: both ends moving up or down together.

Springs, dampers, anti-roll bars, ride heights, and aero loads all influence these motions. Excessive pitch can destabilize braking and aero balance. Excessive roll can reduce consistency and change how the tires are loaded across an axle.

## Center of Gravity
The center of gravity, often shortened to CoG, is the effective point where vehicle mass is considered to act. Its position influences how much load transfer occurs and how that load is distributed.

General effects:

- Higher CoG: larger load transfer for the same acceleration level.
- Lower CoG: smaller load transfer and often better stability.
- Forward CoG bias: more static front load.
- Rearward CoG bias: more static rear load.

Static weight distribution matters, but dynamic behavior matters more. A car that looks balanced on paper can still behave poorly if suspension, tires, and aero shift the dynamic balance in the wrong direction.

## Basic Equations
A few simple relations help frame setup thinking:

- Force relation: \(F = ma\)
- Lateral acceleration in a corner: \(a_y = v^2 / R\)

These equations show why higher speed and tighter radius demand more tire force. They do not replace full modeling, but they explain why the same setup issue may appear only in specific corner types.

## Mechanical Balance
Mechanical balance describes how front and rear grip compare when the car is relying mostly on tires, suspension, and weight transfer rather than strong aerodynamic effects.

A mechanically front-limited car tends toward understeer. A mechanically rear-limited car tends toward oversteer. Setup tools such as springs, anti-roll bars, dampers, tire pressures, and differential settings all influence this balance, directly or indirectly.

## Why This Matters for RAG
For a race engineer assistant, these concepts form a shared vocabulary that links driver comments, telemetry patterns, and setup actions. Most practical setup advice can be traced back to tire force generation, load transfer, and how the car manages pitch, roll, and ride platform.
