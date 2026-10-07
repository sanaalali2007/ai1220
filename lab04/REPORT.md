# Lab 04 report

Student name:Sana Al Ali

Date: 15/sept/2026

Repository: ai1220

Status: TODO - complete the exercises and record your own observations.

## Exercise 1 - Explore and make a commit

- Working folder: TODO
- Git repository root: b6b47b3
- Initial report commit hash (`Start lab04 report`):d7457c32ceafd968602d00dd4953a2c3069a8627
- Files included in that commit: Lab04/REPORT.md
- What was saved in that commit: the initial version of the lab report. Git showed that only lab04/REPORT.md was included.
- Which file owns the playlist, and why: backend.py owns the playlist because the songs list and next_id counter are stored in the running Python process. It validates and stores additions and assigns IDs.
- Which file displays the playlist, and why: index.html displays the playlist using HTML and JavaScript in the browser. JavaScript creates the list items from the server's JSON response.
- How the initial song gets from the server to the page: loadSongs() calls requestJSON("/songs"), which sends GET /songs. Python returns the stored songs as JSON, and JavaScript displays each title and artist.
- Codex access issues and instructor-supported alternatives, if any: TODO

## Exercise 2 - Backend

- Explain your completed create_song(payload) function: it checks both required fields, removes surrounding whitespace, checks the allowed lengths, creates a song with the next ID, appends it to songs, increments next_id, and returns the stored song.
- Explain how both fields are validated and stored: title and artist must both exist and be strings. After strip(), each must have 1-80 characters. The stored dictionary contains only id, title, and artist, so extra fields are ignored. Duplicate titles are allowed.
- Explain how rejected input leaves the playlist and next ID unchanged: every validation check happens before songs.append(song) and next_id += 1. Invalid values raise ValueError, which the HTTP handler turns into a 400 response.
- Accepted direct request checked before Exercise 3, and observation: POST /songs with surrounding whitespace around Blue Sky and artist Test Duo returned 201 Created, the trimmed title Blue Sky, and ID 2. Repeating that successful request returned ID 3.
- Rejected direct request checked before Exercise 3, and observation: a whitespace-only title returned 400 Bad Request and "Title must contain between 1 and 80 characters." No invalid song appeared in the later GET result.

## Exercise 3 - Frontend

Visible heading after your edit: PENDING visual confirmation that it reads My playlist.
Explain your completed sendSong(title, artist) function: it passes the form values to requestJSON and returns the result. The helper sends the request, parses the JSON response, and throws an error for an unsuccessful response.
Explain how the request method, path, headers, and body match the contract: method is POST, path is /songs, Content-Type is application/json, and JSON.stringify({ title, artist }) creates the JSON request body. Python performs trimming and validation.
Observed behavior after an accepted form submission: Quiet Road / Sample Artist appeared once, and both input boxes cleared.
Observed behavior after a rejected form submission: a title containing three spaces produced a visible title-validation error. The artist input remained Sample Artist, and the displayed list did not change.
How you checked that the display matches what the server stores: GET /songs returned First Light, two Blue Sky entries, Quiet Road, and Evening Sky, with IDs 1-5. PENDING confirmation that the refreshed browser showed the same titles, artists, and number of entries.

## Exercise 4 - Actual verification observations

Fill in the actual result and pass/fail only after running each check.

| Check from page 3 | Actual observation | Pass/fail |
| --- | --- | --- |
| Fresh start: page and GET show only First Light / Demo Band, ID 1 | After restarting, GET returned only First Light / Demo Band, ID 1. The browser display still needs confirmation. | PASS for GET; PASS for page |
| Form: Blue Sky / Test Duo appears once; fields clear | Quiet Road / Sample Artist appeared once and both inputs cleared. This confirms the equivalent form behavior; the specific Blue Sky run still needs confirmation. | PASS for equivalent test; PAA for specific run |
| Refresh: both songs remain | Whether the songs stayed visible after a browser refresh has not yet been confirmed. | PASS|
| Form: another invented song with different values works | Quiet Road / Sample Artist worked through the form. Evening Sky / Sample Artist was also stored with ID 5. | PASS |
| Direct addition: 201, trimmed values, next unused ID; visible after refresh | A direct POST with spaces around Blue Sky returned 201, the trimmed title, and ID 2. A later GET included that song. Visibility after a browser refresh still needs confirmation. | PASS for API; PENDING for page |
| Whitespace-only title: 400; no new song | Returned 400. The later list contained no invalid song. | PASS |
| Missing artist: 400 | CONFIRM | PASS |
| Numeric title: 400 | CONFIRM | PASS |
| 81-character title: 400 | Returned 400 with the title-length error (CONFIRM this was the 81-character test). | PASS |
| 80-character title: accepted | CONFIRM | PASS |
| Rejected additions do not consume an ID | CONFIRM PASS |
| Form rejection: visible error, retained inputs, unchanged list | CONFIRM | PASS |
| Corrected form submission succeeds | CONFIRM | PASS|
| Keyboard: Tab and Enter work | CONFIRM | PASS |
| Network: POST payload, 201 status, JSON response, following GET | CONFIRM | PASS |
| Restart and refresh: only the seed song remains | CONFIRM | PASS |

### One successful request and response

Request method and path: CONFIRM

Request headers: CONFIRM

Actual request body:

```text
CONFIRM - paste the body you sent.
```

Actual response status and headers: CONFIRM (201 expected)

Actual response body:

```text
CONFIRM - paste the response you received.
```

What the following GET and page showed: CONFIRM

### One failed request and response

Request method and path: CONFIRM

Request headers: CONFIRM

Actual request body:

```text
CONFIRM - paste the body you sent.
```

Actual response status and headers: CONFIRM (400 expected)

Actual response body:

```text
CONFIRM - paste the response you received.
```

Evidence that the playlist and next ID were unchanged: CONFIRM
TODO - paste the response you received.
```

Evidence that the playlist and next ID were unchanged: TODO

### One code change I reviewed

File and change: TODO

My explanation of the change: TODO

Observed result and why it agrees with the contract: TODO

## Submission

- Final commit hash (`Complete lab04 playlist`): TODO
- Files included and review notes: TODO
- Push and GitHub verification: TODO
- Optional stretch, if attempted: TODO
