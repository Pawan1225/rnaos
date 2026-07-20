"use client";

import { useEffect, useState } from "react";
import { getHealth } from "@/lib/api";

export default function Home() {
  const [health, setHealth] = useState<unknown>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadHealth() {
      try {
        const data = await getHealth();
        setHealth(data);
      } catch (err) {
        console.error("API Error:", err);

        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError("Failed to fetch");
        }
      }
    }

    loadHealth();
  }, []);

  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 text-white">
      <div className="w-full max-w-2xl rounded-xl border border-slate-700 bg-slate-900 p-8 shadow-lg">
        <h1 className="mb-6 text-4xl font-bold">RNAOS</h1>

        {error ? (
          <div>
            <p className="mb-2 text-red-400 font-semibold">Error</p>
            <pre className="rounded bg-black p-4 text-red-300">
              {error}
            </pre>
          </div>
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
