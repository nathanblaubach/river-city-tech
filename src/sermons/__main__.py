from sermons.instructions_generator import InstructionsGenerator
from sermons.recording_editor import RecordingEditor
from sermons.recording_metadata_form import RecordingMetadataForm
from sermons.recording_upload_bundle_writer import RecordingUploadBundleWriter
from sermons.video_generator import VideoGenerator


def main():
    recording = RecordingEditor(
        RecordingMetadataForm(),
        RecordingUploadBundleWriter(VideoGenerator(), InstructionsGenerator()),
    )
    recording.prepare_for_upload()


if __name__ == "__main__":
    main()
