const API_BASE = "http://127.0.0.1:8000";

export async function getHealth() {
  const response = await fetch(`${API_BASE}/api/v1/health/`);

  if (!response.ok) {
    throw new Error("Backend unavailable");
  }

  return response.json();
}
