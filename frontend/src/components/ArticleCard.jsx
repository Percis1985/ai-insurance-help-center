import { Link } from "react-router-dom";

function ArticleCard({ article }) {
  return (
    <div className="bg-white border rounded-xl p-5 shadow-sm hover:shadow-md transition">
      <p className="text-sm text-blue-600 font-medium">{article.category}</p>
      <h3 className="text-lg font-semibold mt-2">{article.title}</h3>
      <p className="text-gray-600 mt-2 line-clamp-3">
        {article.content}
      </p>

      <Link
        to={`/articles/${article.id}`}
        className="inline-block mt-4 text-blue-700 font-medium"
      >
        Read more →
      </Link>
    </div>
  );
}

export default ArticleCard;