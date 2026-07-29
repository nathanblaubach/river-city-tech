# River City Tech

## Purpose

The tools in this repository reduce the amount of manual work required for technical tasks at River City Church.

### Lessons

Slows down the videos from our curriculum to allow kids to understand the Bible lessons better

### Sermons

Generates sermon upload artifacts and instructions for soundcloud and youtube to

* Eliminate the need to use a fully-fledged video editor
* Eliminate the manual crafting of differing naming conventions of titles and descriptions for soundcloud and youtube

## Setup/Run

You will need to have [uv](https://docs.astral.sh/uv/getting-started/installation/) and [FFmpeg](https://ffmpeg.org/download.html) installed.

Set up source code and dependencies

```shell
git clone https://github.com/nathanblaubach/sermons.git
cd sermons
uv sync
uv run pre-commit install
```

Run the applications

```shell
uv run lessons
uv run sermons
```

Run quality checks

```shell
uv run pre-commit run --all-files # Formatting / Linting
uv run pytest                     # Unit tests and coverage
```
