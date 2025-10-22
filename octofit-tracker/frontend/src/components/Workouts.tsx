import React, { useEffect, useState } from 'react';

type Workout = { id: string; user: string; type: string; duration: number; date: string };

const Workouts: React.FC = () => {
  const [data, setData] = useState<Workout[]>([]);
  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const base = codespace ? `https://${codespace}-8000.app.github.dev` : '';
    const url = `${base}/api/workouts/`;
    console.log('Fetching workouts from', url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log('Workouts response', json);
        const items = Array.isArray(json) ? json : json.results || [];
        setData(items);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="container mt-3">
      <h2>Workouts</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Type</th>
            <th>Duration</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {data.map((w) => (
            <tr key={w.id}>
              <td>{w.id}</td>
              <td>{w.user}</td>
              <td>{w.type}</td>
              <td>{w.duration}</td>
              <td>{w.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Workouts;
