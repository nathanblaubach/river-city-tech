import sys
from pathlib import Path

from sermons.instructions_generator import InstructionsGenerator
from sermons.recording_editor import RecordingEditor
from sermons.recording_metadata import RecordingMetadata
from sermons.recording_metadata_form import RecordingMetadataForm
from sermons.recording_upload_bundle_writer import RecordingUploadBundleWriter
from sermons.video_generator import VideoGenerator


class FakeRecordingMetadataForm(RecordingMetadataForm):
    def get_metadata(self) -> RecordingMetadata | None:
        return RecordingMetadata(
            audio_file_path=Path(__file__).parent / "test" / "test-recording.mp3",
            title="Test Recording",
            date="2026.02.25",
            speaker_name="Nathan Blaubach",
        )


def main():
    metadata_form = (
        FakeRecordingMetadataForm() if "--test" in sys.argv else RecordingMetadataForm()
    )
    recording = RecordingEditor(
        metadata_form,
        RecordingUploadBundleWriter(VideoGenerator(), InstructionsGenerator()),
    )
    recording.prepare_for_upload()


if __name__ == "__main__":
    main()
