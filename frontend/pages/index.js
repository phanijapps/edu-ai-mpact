import { useState } from 'react';

export default function Home() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const send = async () => {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    const data = await res.json();
    setResponse(data.response || data.detail);
  };

  return (
    <main style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'Arial' }}>
      <h1>Edu AI Mpact</h1>
      <textarea
        style={{ width: '100%', height: 120 }}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={send} style={{ marginTop: '0.5rem' }}>Send</button>
      <pre style={{ background: '#f1f1f1', padding: '1rem' }}>{response}</pre>
    </main>
  );
}
