import React, { useEffect, useState } from 'react';

type Team = { id: string; name: string; created_at: string };

const Teams: React.FC = () => {
  const [data, setData] = useState<Team[]>([]);
  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const base = codespace ? `https://${codespace}-8000.app.github.dev` : '';
    const url = `${base}/api/teams/`;
    console.log('Fetching teams from', url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log('Teams response', json);
        const items = Array.isArray(json) ? json : json.results || [];
        setData(items);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="container mt-3">
      <h2>Teams</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Created At</th>
          </tr>
        </thead>
        <tbody>
          {data.map((t) => (
            <tr key={t.id}>
              <td>{t.id}</td>
              <td>{t.name}</td>
              <td>{t.created_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Teams;
