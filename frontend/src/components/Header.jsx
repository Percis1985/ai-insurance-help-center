import { Link } from "react-router-dom";

function Header() {
  return (
    <header className="bg-white shadow-sm border-b">
      <div className="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-blue-700">
          AI Insurance Help Center
        </Link>

        <nav className="flex gap-6 text-gray-700">
          <Link to="/" className="hover:text-blue-700">Home</Link>
          <Link to="/topics" className="hover:text-blue-700">Topics</Link>
          <Link to="/assistant" className="hover:text-blue-700">AI Assistant</Link>
        </nav>
      </div>
    </header>
  );
}

export default Header;