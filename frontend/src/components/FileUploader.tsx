"use client";
import { FileUpload, FileUploadUploadEvent } from "primereact/fileupload";

export default function FileUploader() {
  const onUpload = (e: FileUploadUploadEvent) => {
    console.log("Uploaded!");
    console.log(e);
  };

  return (
    <FileUpload
      mode="basic"
      name="resume"
      accept="*.pdf"
      maxFileSize={1000000}
      onUpload={onUpload}
    />
  );
}
