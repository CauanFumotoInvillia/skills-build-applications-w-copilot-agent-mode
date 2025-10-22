import React, { useEffect, useState } from 'react';

type User = { id: string; username: string; email: string; team?: string };

const Users: React.FC = () => {
  const [data, setData] = useState<User[]>([]);
  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const base = codespace ? `https://${codespace}-8000.app.github.dev` : '';
    const url = `${base}/api/users/`;
    console.log('Fetching users from', url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log('Users response', json);
        const items = Array.isArray(json) ? json : json.results || [];
        setData(items);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="container mt-3">
      <h2>Users</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
            <th>Team</th>
          </tr>
        </thead>
        <tbody>
          {data.map((u) => (
            <tr key={u.id}>
              <td>{u.id}</td>
              <td>{u.username}</td>
              <td>{u.email}</td>
              <td>{(u as any).team || ''}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Users;
