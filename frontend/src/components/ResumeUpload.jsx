import { useState } from "react";
import { analyzeResume } from "../api/resumeApi";

const ResumeUpload = ({ onResult }) => {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!resume || !jobDescription) {
      alert("Please upload resume and enter job description");
      return;
    }

    setLoading(true);
    try {
      const result = await analyzeResume(resume, jobDescription);
      onResult(result);
    } catch (err) {
      console.error(err);
      alert("Resume analysis failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setResume(e.target.files[0])}
      />
      <br /><br />

      <textarea
        placeholder="Paste Job Description here"
        rows="8"
        cols="60"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />
      <br /><br />

      <button type="submit" disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>
    </form>
  );
};

export default ResumeUpload;
