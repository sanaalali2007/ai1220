# Campus Workshop Board - Design notes

Name: [Sana Al Ali ]
Student ID: [25011167]

Let the diagrams carry the explanation. Complete only these short notes.

## Diagram files

| View | Editable source (and page if needed) | Export |
|---|---|---|
| 01-context | diagrams/source/01-context.svg | diagrams/exports/01-context.png |
| 02-containers | diagrams/source/02-containers.svg | diagrams/exports/02-containers.png |
| 03-components | diagrams/source/03-components.svg | diagrams/exports/03-components.png |
| 04-code | diagrams/source/04-code.svg | diagrams/exports/04-code.png |
| 05-dynamic | diagrams/source/05-dynamic.svg | diagrams/exports/05-dynamic.png |

Each SVG is one editable vector canvas with separate text, shapes and lines (open in Inkscape); PNGs are rendered from those sources. No multi-page files. W17, S23 and R-new are readable aliases for identifiers, not literal UUID values. External HTTPS/JSON interfaces are assumed contracts for this design.

## One structural choice (Exercise 2)

One server-rendered Django application and one PostgreSQL database keep deployment and maintenance small for 200 students while providing durable, transactional seat allocation.

## Your components (Exercise 3)

| Name | Job | Customer rule(s) served |
|---|---|---|
| Web Controller | Authenticate every board request before dispatch; render summaries (title, time, capacity, remaining seats, own reservation) and outcomes; never trust a client-supplied student ID. | R1, R3, R4, R6 |
| Identity Gateway | Verify credentials with Campus Identity; establish and validate a signed session carrying the verified student ID, name and email; reject invalid sessions. | R1, R4 |
| Workshop Service | Create unique-ID workshops with creator as owner, nonempty title, required start and capacity 1–20; authorise publish and attendee access against stored owner ID; publishing inserts no reservation. Browse only published workshops; include contacts only in the owner's attendee response. | R2, R3 |
| Reservation Service | Return existing reservations unchanged; allocate at most one seat within capacity; request confirmation only for a newly committed reservation. | R4, R6 |
| Board Repository | Persist workshops, ownership and reservations; provide transactional row locking and unique keys; query stored state on refresh, including remaining-seat counts and own reservation in one consistent read. | R2, R3, R4, R5 |
| Mail Gateway | Submit one confirmation request containing recipient and workshop/reservation details; map failure/timeout to Unavailable, without automatic retries. | R6 |

## Reservation operation (Exercise 4)

`ReservationRules.reserve(student: VerifiedStudent, workshopId: UUID) -> ReservationResult`.

Results: `Created(reservation, Accepted | Unavailable)`, `Existing(reservation)`, `NotFound`, `NotPublished`, `Full`, or `StorageFailure`. An unverified request returns HTTP 401 from Web Controller **before** this operation; it changes no reservations. Types and relationships appear in `04-code`.

Invariant: for each workshop W, `0 <= reservationCount(W) <= capacity(W)` and at most one reservation for `(workshopId, studentId)`. In one READ COMMITTED transaction, lock W with `SELECT ... FOR UPDATE`; then read the existing reservation **before** testing fullness. If existing, finish without updates or email. Otherwise reject missing/unpublished/full workshops, or insert one reservation and commit. Every allocator holds the same workshop-row lock until transaction end, so overlapping calls run their checks in turn and see earlier committed inserts. A database unique constraint on `(workshopId, studentId)` additionally prevents duplicates. Capacity changes, cancellation and deletion are outside this design's scope.

Only after a new reservation commits does Reservation Service call Mail Gateway. Mail failure never rolls the reservation back. A subsequent verified repeat returns that same reservation without sending another email. Database failures roll back unfinished allocation transactions. Committed records survive application restart; refresh reads them again.

## Ari's incident (Exercise 5)

| Observation | Result |
|---|---|
| Stored state before | W17, “Build a tiny game”: owner S10; published; capacity 3; reservations for S21 and S22; remaining seats 1; none for S23. |
| Stored state after | Same workshop, owner and capacity. S21/S22 reservations unchanged; new R-new for S23, name Ari, email ari@example.invalid. Total 3; remaining seats 0. Mail unavailable; no rollback and no retry scheduled. S10 has no seat merely by being owner. |
| Message Ari sees | “Reservation successful for ‘Build a tiny game’. Your seat is reserved, but confirmation email is unavailable.” On refresh, Ari sees their stored reservation and 0 remaining seats. |
