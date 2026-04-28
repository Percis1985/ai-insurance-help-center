import { useState } from "react";
import { Link } from "react-router-dom";
import apiClient from "../api/apiClient";
import SearchBar from "../components/SearchBar";
import ArticleCard from "../components/ArticleCard";

function Home() {
  const [results, setResults] = useState([]);
  const [searched, setSearched] = useState(false);

  const handleSearch = async (query) => {
    try {
      const response = await apiClient.get(`/search/?q=${query}`);
      setResults(response.data);
      setSearched(true);
    } catch (error) {
      console.error("Search failed", error);
    }
  };

  return (
    <div>
      <section className="bg-blue-50 py-16">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <h1 className="text-4xl font-bold text-gray-900">
            How can we help with your insurance today?
          </h1>

          <p className="text-gray-600 mt-4">
            Search help articles, browse insurance topics, or ask our AI assistant.
          </p>

          <div className="mt-8">
            <SearchBar onSearch={handleSearch} />
          </div>

          <Link
            to="/assistant"
            className="inline-block mt-6 bg-blue-700 text-white px-6 py-3 rounded-lg"
          >
            Ask AI Assistant
          </Link>
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-4 py-10">
        {searched && (
          <>
            <h2 className="text-2xl font-bold mb-5">Search Results</h2>

            {results.length === 0 ? (
              <p className="text-gray-600">No articles found.</p>
            ) : (
              <div className="grid md:grid-cols-2 gap-5">
                {results.map((article) => (
                  <ArticleCard key={article.id} article={article} />
                ))}
              </div>
            )}
          </>
        )}

        {!searched && (
          <>
            <h2 className="text-2xl font-bold mb-5">Popular Help Topics</h2>

            <div className="grid md:grid-cols-3 gap-5">
              {["Claims", "Travel", "Policy", "Life Insurance", "Motor Insurance"].map(
                (topic) => (
                  <Link
                    key={topic}
                    to="/topics"
                    className="bg-white border rounded-xl p-6 shadow-sm hover:shadow-md"
                  >
                    <h3 className="font-semibold text-lg">{topic}</h3>
                    <p className="text-gray-600 mt-2">
                      Browse common questions about {topic}.
                    </p>
                  </Link>
                )
              )}
            </div>
          </>
        )}
      </section>
    </div>
  );
}

export default Home;