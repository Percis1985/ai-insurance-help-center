import ChatBox from "../components/ChatBox";

function Assistant() {
  return (
    <div className="max-w-4xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold">AI Insurance Assistant</h1>

      <p className="text-gray-600 mt-2 mb-6">
        Ask questions about claims, policy terms, travel insurance, or life insurance.
      </p>

      <ChatBox />
    </div>
  );
}

export default Assistant;