"use client";

import { useEffect, useState } from "react";
import { getHealth } from "@/lib/api";

export default function Home() {
  const [health, setHealth] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    getHealth()
      .then(setHealth)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 text-white">
      <div className="rounded-xl border border-slate-700 bg-slate-900 p-8 shadow-lg">
        <h1 className="mb-6 text-4xl font-bold">RNAOS</h1>

        {error ? (
          <p className="text-red-400">{error}</p>
        ) : health ? (
          <pre className="rounded bg-black p-4 text-green-400">
            {JSON.stringify(health, null, 2)}
          </pre>
        ) : (
          <p className="text-slate-400">Connecting to backend...</p>
        )}
      </div>
    </main>
  );
}
