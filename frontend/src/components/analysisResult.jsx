const AnalysisResult = ({ result }) => {
  if (!result) return null;

  if (result.error) {
    return (
      <div style={{ color: "red" }}>
        <strong>Error:</strong> {result.details || result.error}
      </div>
    );
  }

  return (
    <div>
      <h2>ATS Analysis Result</h2>
      <p><strong>Score:</strong> {result.rank}%</p>

      <h4>Skills</h4>
      <ul>
        {result.skills?.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      <p><strong>Total Experience:</strong> {result.total_experience}</p>

      <h4>Project Categories</h4>
      <ul>
        {result.project_category?.map((cat, index) => (
          <li key={index}>{cat}</li>
        ))}
      </ul>
    </div>
  );
};

export default AnalysisResult;
