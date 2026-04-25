# Setup for Understeer and Oversteer

## Purpose
This document defines understeer and oversteer in neutral, car-agnostic terms and explains how common setup levers affect them. It is intended as a first-pass guide for diagnosis and adjustment logic.

## Definitions
Understeer means the front tires run out of grip before the rear tires. The driver asks for more steering angle, but the car does not rotate enough.

Oversteer means the rear tires run out of grip before the front tires. The rear rotates more than intended, and the driver may need steering correction to catch the slide.

Neutral balance sits between the two. In practice, most race cars are tuned for a small amount of safe understeer in at least some phases of the corner.

## Corner Phases
Balance should be analyzed by phase, because the same car can understeer in one phase and oversteer in another.

- Corner entry: initial braking release and turn-in.
- Mid-corner: steady-state cornering at partial or maintenance throttle.
- Corner exit: throttle application and power delivery.

Examples:

- Entry understeer: the car resists rotation on turn-in.
- Entry oversteer: the rear becomes unstable during trail braking.
- Mid-corner understeer: the front washes wide at steady steering.
- Exit oversteer: the rear breaks loose when throttle is applied.

## Typical Driver Language
Common phrases that often map to balance issues:

- “The front washes out” usually suggests understeer.
- “The rear is loose” usually suggests oversteer.
- “It will not rotate” usually points to entry or mid-corner understeer.
- “It snaps on throttle” usually points to exit oversteer.
- “It feels nervous on entry” often points to rear instability under braking.

These are useful signals, but they should always be checked against telemetry and test conditions.

## Common Causes of Understeer
Generic causes include:

- Front tires overloaded relative to rear tires.
- Front tire pressures too high or outside the useful operating window.
- Front suspension or front anti-roll bar too stiff for the available grip.
- Rear too soft in roll relative to front.
- Insufficient front aero load at high speed.
- Differential behavior that prevents rotation on entry or exit.
- Driving line or brake release timing that keeps too much load on the front axle.

## Common Causes of Oversteer
Generic causes include:

- Rear tires overloaded relative to front tires.
- Rear tire pressures too high or outside the useful operating window.
- Rear suspension or rear anti-roll bar too stiff for the available grip.
- Rear aero support too weak at speed.
- Aggressive coast or power differential behavior.
- Abrupt throttle or brake release.
- Excessive rear ride-height sensitivity.

## Adjustment Directions
These are broad tendencies, not universal rules.

To reduce understeer:

- Increase front grip.
- Reduce rear grip advantage.
- Shift roll stiffness balance rearward only if the platform remains stable.
- Add front aero load or reduce excessive rear aero bias when high-speed behavior supports it.
- Revisit front tire pressures and temperature distribution.

To reduce oversteer:

- Increase rear grip.
- Reduce front grip advantage.
- Shift roll stiffness balance forward only if the car still rotates enough.
- Add rear aero load when the issue appears mainly at speed.
- Revisit rear tire pressures and traction conditions.

## Common Setup Levers
Typical balance tendencies:

- Stiffer front anti-roll bar: tends to increase understeer.
- Stiffer rear anti-roll bar: tends to increase oversteer.
- More front spring or front platform stiffness: often reduces front grip over uneven surfaces and can add understeer.
- More rear spring or rear platform stiffness: often reduces rear grip and can add oversteer.
- More rear wing: tends to increase rear stability in medium and high-speed corners.
- Lower front ride height or stronger front aero platform: can improve front bite if the aero map supports it.

These effects depend on speed range, tire model, suspension geometry, and track surface.

## Diagnostic Approach
Use a repeatable process:

1. Identify the exact corner phase where the issue appears.
2. Separate low-speed and high-speed behavior.
3. Check tire pressures and temperatures before changing hard parts.
4. Change one major variable at a time.
5. Confirm the effect over several laps, not one lap.

## Practical Note
A car should not be tuned only around the sharpest problem corner. A better target is a balance that the driver can trust repeatedly across the lap, especially in braking zones, long loaded corners, and traction zones.
