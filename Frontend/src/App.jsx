import React, { useEffect, useState } from "react";
import axios from "axios";
import UrlCard from "./Component/Card";

function App() {
  const [url, setUrl] = useState("");
  const [urls, setUrls] = useState([]);
  const baseURL = "http://127.0.0.1:8000";

  const fetchUrls = async () => {
    try {
      const res = await axios.get(`${baseURL}/geturl/`);
      setUrls(res.data?.data);
      console.log("yes", res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const createUrl = async (e) => {
    e.preventDefault();
    if (!url.trim()) return;
    try {
      await axios.post(`${baseURL}/posturl/`, { long: url });
      setUrl("");
      fetchUrls();
    } catch (err) {
      console.error(err);
    }
  };

  const deleteUrl = async (id) => {
    try {
      await axios.delete(`${baseURL}/delete/${id}/`);
      fetchUrls();
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchUrls();
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-lg p-6">
        <h2 className="text-2xl font-semibold text-center mb-6">
          URL Shortener
        </h2>

        <form onSubmit={createUrl} className="flex mb-6">
          <input
            type="text"
            value={url}
            placeholder="Enter URL"
            onChange={(e) => setUrl(e.target.value)}
            className="flex-1 px-4 py-2 border border-gray-300 rounded-l-lg focus:outline-none "
          />
          <button
            type="submit"
            className="px-4 py-2 bg-blue-500 text-white rounded-r-lg hover:bg-blue-600 transition-colors"
          >
            Shorten
          </button>
        </form>

        <div>
          <h3 className="text-xl font-medium mb-4">All Shortened URLs</h3>
          {urls.length === 0 ? (
            <p className="text-gray-500 text-center">No URLs shortened yet.</p>
          ) : (
            urls.map((u) => (
              <UrlCard key={u.id} urlData={u} onDelete={deleteUrl} />
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
