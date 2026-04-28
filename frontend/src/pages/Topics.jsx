import { useEffect, useState } from "react";
import apiClient from "../api/apiClient";
import ArticleCard from "../components/ArticleCard";

function Topics() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    loadArticles();
  }, []);

  const loadArticles = async () => {
    const response = await apiClient.get("/articles/");
    setArticles(response.data);
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold">Insurance Help Topics</h1>
      <p className="text-gray-600 mt-2">
        Browse articles related to claims, travel insurance, policy terms, and life insurance.
      </p>

      <div className="grid md:grid-cols-2 gap-5 mt-8">
        {articles.map((article) => (
          <ArticleCard key={article.id} article={article} />
        ))}
      </div>
    </div>
  );
}

export default Topics;