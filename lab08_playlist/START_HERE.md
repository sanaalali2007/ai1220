# Your finished Lab 08

Ilina Krumova: backend. Sana Ali: frontend.
The backend, API contract and team file are from IlinaKrumova/ai1220.
The completed index.html matches that backend. The original project setup files are included.

1. Extract this ZIP. Put lab08_playlist inside your own ai1220 repository.
   If that folder already exists, back it up first and copy these files into it.
2. Open Terminal and run:

```sh
cd ~/ai1220/lab08_playlist
uv sync --frozen
uv run python backend.py
```

If your repository is elsewhere, use its actual path instead.
3. Open http://127.0.0.1:8000 in your browser. Keep Terminal running.
4. Try adding a song, voting, and adding with an empty field.
5. Send index.html to Ilina so she can add it to her own folder.
6. Stop the server with Control+C. From your lab08_playlist folder:

```sh
cd ..
git add lab08_playlist
git commit -m "Complete Lab 8 playlist frontend"
git push
```

Each partner pushes the whole app to their own repository.
Restarting the server resets songs and votes.

## Frontend functions

- loadPlaylist(): GET /songs, then create one card for each returned song.
- addSong(): POST the entered title and artist; clear the fields on success and reload.
- vote(id): POST /songs/{id}/votes and reload the playlist.
- Errors: show the exact error message returned by Ilina's backend.

Verified against Ilina's backend: extra songs added through the API appear;
adding clears both fields; voting increases the total; invalid adds and missing
song votes display the backend's exact messages. These checks used JavaScript
with a simulated document and real HTTP requests, rather than a visual browser test.
