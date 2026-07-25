# Sermons

## Purpose

Reduce the amount of manual work in the recording upload process

Given a recording's audio file title, date, and speaker name, this application generates:

* Soundcloud Artwork and Audio File
* Youtube Thumbnail and Video
* Upload Instructions with values for Soundcloud and Youtube upload fields

This allows the upload process to happen without the need for manually

* Creating the video with a fully-fledged video editor
* Crafting the differing naming conventions of the titles and descriptions for soundcloud and youtube

## Setup

You will need to have [uv](https://docs.astral.sh/uv/getting-started/installation/) and [FFmpeg](https://ffmpeg.org/download.html) installed.

Clone the repository

```shell
# Clone this repository and switch to the directory
git clone https://github.com/nathanblaubach/sermons.git
cd sermons
```

Set up dependencies

```shell
# Install dependencies
uv sync

# Install pre-commit hook
uv run pre-commit install
```

Run the application

```shell
uv run src/__main__.py
```

Run quality checks

Builds will fail if any formatting, linting or test issues arise. Coverage must stay at 100% for unit testable code.

```shell
uv run pre-commit run --all-files # Formatting / Linting
uv run pytest # Unit tests and coverage
```

## Contributors

- [Nathan Blaubach](https://github.com/nathanblaubach)

## Licenses

- [MIT](https://github.com/nathanblaubach/sermons/blob/main/LICENSE)
