import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import apiClient from "../api/apiClient";

function ArticleDetails() {
  const { id } = useParams();
  const [article, setArticle] = useState(null);

  useEffect(() => {
    loadArticle();
  }, [id]);

  const loadArticle = async () => {
    const response = await apiClient.get(`/articles/${id}`);
    setArticle(response.data);
  };

  if (!article) {
    return <div className="p-10">Loading article...</div>;
  }

  return (
    <div className="max-w-3xl mx-auto px-4 py-10">
      <p className="text-blue-700 font-medium">{article.category}</p>

      <h1 className="text-3xl font-bold mt-2">{article.title}</h1>

      <div className="bg-white border rounded-xl p-6 mt-6 shadow-sm">
        <p className="text-gray-700 leading-7 whitespace-pre-line">
          {article.content}
        </p>
      </div>

      <Link
        to="/assistant"
        className="inline-block mt-6 bg-blue-700 text-white px-6 py-3 rounded-lg"
      >
        Ask AI about this topic
      </Link>
    </div>
  );
}

export default ArticleDetails;