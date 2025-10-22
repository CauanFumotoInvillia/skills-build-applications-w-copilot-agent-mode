import React, { useEffect, useState } from 'react';

type Activity = {
  id: string;
  user: string;
  name: string;
  duration: number;
  distance?: number | null;
  date: string;
};

const Activities: React.FC = () => {
  const [data, setData] = useState<Activity[]>([]);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const base = codespace ? `https://${codespace}-8000.app.github.dev` : '';
    const url = `${base}/api/activities/`;
    console.log('Fetching activities from', url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log('Activities response', json);
        const items = Array.isArray(json) ? json : json.results || [];
        setData(items);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="container mt-3">
      <h2>Activities</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Name</th>
            <th>Duration</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {data.map((a) => (
            <tr key={a.id}>
              <td>{a.id}</td>
              <td>{a.user}</td>
              <td>{a.name}</td>
              <td>{a.duration}</td>
              <td>{a.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Activities;
