import React, { useEffect, useState } from 'react';

type Entry = { id: string; user: string; score: number; date: string };

const Leaderboard: React.FC = () => {
  const [data, setData] = useState<Entry[]>([]);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const base = codespace ? `https://${codespace}-8000.app.github.dev` : '';
    const url = `${base}/api/leaderboard/`;
    console.log('Fetching leaderboard from', url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log('Leaderboard response', json);
        const items = Array.isArray(json) ? json : json.results || [];
        setData(items);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="container mt-3">
      <h2>Leaderboard</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Score</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {data.map((e) => (
            <tr key={e.id}>
              <td>{e.id}</td>
              <td>{e.user}</td>
              <td>{e.score}</td>
              <td>{e.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Leaderboard;
