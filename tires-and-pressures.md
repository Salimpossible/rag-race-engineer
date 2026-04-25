# Tires and Pressures

## Purpose
This document covers generic tire behavior and pressure tuning logic for race setup work. Tires are usually the largest source of lap time variation and the first place to check before larger setup changes.

## Why Tires Matter
Tires create the forces for braking, turning, and acceleration. Their performance changes continuously with pressure, temperature, load, slip, wear, and track condition.

A setup that looks correct elsewhere can still fail if the tires operate outside their useful window. For that reason, tire pressures and temperatures should be treated as foundational setup variables.

## Contact Patch
The contact patch is the tire area touching the track. It is small, but it carries all acceleration, braking, and cornering forces.

Pressure influences the contact patch:

- Higher pressure usually reduces patch size and makes the tire more responsive, but can reduce peak grip.
- Lower pressure usually increases patch size and can improve grip potential, but may increase heat buildup and carcass movement.

The ideal pressure is not simply “as low as possible” or “as high as possible.” It is the pressure that lets the tire work efficiently and consistently over the intended run length.

## Cold and Hot Pressures
Cold pressure is the reading before the tire is fully up to operating temperature. Hot pressure is the reading after running.

In most race engineering workflows, the target is a hot-pressure operating window rather than a cold number by itself. The cold value is only a starting point used to reach the desired hot value.

Important influences on pressure rise:

- Ambient temperature.
- Track temperature.
- Run length.
- Driving style.
- Vehicle mass and fuel load.
- Sliding and wheelspin.
- Camber and toe settings.

## Temperature Behavior
Tire temperature should be interpreted carefully. A single overall tire temperature is less useful than a pattern.

Useful observations:

- All tires too cool: pressures may be low, pace may be low, or the track may not be demanding enough.
- All tires too hot: pressures may be wrong, sliding may be excessive, or the setup may overload the tire.
- Front hotter than rear: the car may be front-limited or driven in a way that overloads the front axle.
- Rear hotter than front: the car may be traction-limited or rear-limited.
- Large left-right differences: the track layout or corner mix may be the main cause.

If inner, middle, and outer temperature bands are available, they can provide clues about pressure and camber behavior.

## Pressure Tuning Tendencies
Generic tendencies only:

- Higher pressure can sharpen response and reduce sidewall movement.
- Higher pressure can also reduce compliance and make the tire easier to overheat through sliding.
- Lower pressure can improve compliance and mechanical grip on rough surfaces.
- Lower pressure can also make the tire less stable and slower to react.

The correct choice depends on the tire model, track surface, and stint objective.

## Wear and Consistency
Pressure affects not only peak grip but also consistency over time. A pressure that produces one strong lap may overheat the tire and reduce performance later in the run.

Watch for:

- Lap-time drop-off across the run.
- Pressure growth that keeps climbing.
- Localized overheating.
- Rear traction falling away after repeated exits.
- Front push increasing as the stint develops.

## Interaction with Setup
Tires do not operate alone. Their behavior is shaped by many surrounding variables:

- Camber changes the loaded footprint and temperature spread.
- Toe affects drag, response, and heat generation.
- Dampers influence how well the tire follows the road surface.
- Springs and anti-roll bars change load transfer distribution.
- Aero load changes the vertical load at speed.

Because of this, pressure tuning should usually happen after a stable baseline is established, but before more complicated interpretation of balance.

## Testing Method
A simple testing method:

1. Start from a known baseline pressure set.
2. Run a controlled stint with consistent fuel and push level.
3. Record hot pressures, tire temperatures, and driver comments.
4. Adjust in small steps.
5. Re-test in similar conditions.

Pressure work becomes unreliable when weather, fuel, traffic, or driving style vary too much between runs.

## Practical Note
Do not use pressures only to hide a major balance problem caused by springs, bars, ride heights, or aero. Tire pressure is powerful, but it works best as a fine-tuning tool around a fundamentally sound platform.
