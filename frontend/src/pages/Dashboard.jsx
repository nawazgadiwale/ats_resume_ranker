import { useState } from "react";
import ResumeUpload from "../components/ResumeUpload";
import AnalysisResult from "../components/analysisResult";

const Dashboard = () => {
  const [analysisResult, setAnalysisResult] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>ATS Resume Ranker</h1>

      <ResumeUpload onResult={setAnalysisResult} />

      {analysisResult && (
        <AnalysisResult result={analysisResult.data} />
      )}
    </div>
  );
};

export default Dashboard;
