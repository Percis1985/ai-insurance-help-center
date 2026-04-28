import { useState } from "react";
import apiClient from "../api/apiClient";

function ChatBox() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi! Ask me any insurance-related question.",
    },
  ]);

  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const sendQuestion = async (e) => {
    e.preventDefault();

    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      text: question,
    };

    setMessages((prev) => [...prev, userMessage]);
    setQuestion("");
    setLoading(true);

    try {
      const response = await apiClient.post("/chat/", {
        question,
      });

      const assistantMessage = {
        role: "assistant",
        text: response.data.answer,
        sources: response.data.sources,
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Sorry, something went wrong. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white border rounded-xl shadow-sm p-5">
      <div className="h-[400px] overflow-y-auto space-y-4 mb-4">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`p-4 rounded-lg ${
              msg.role === "user"
                ? "bg-blue-700 text-white ml-16"
                : "bg-gray-100 text-gray-800 mr-16"
            }`}
          >
            <p className="whitespace-pre-line">{msg.text}</p>

            {msg.sources && msg.sources.length > 0 && (
              <div className="mt-3 text-sm">
                <strong>Sources:</strong>
                <ul className="list-disc ml-5">
                  {msg.sources.map((source, i) => (
                    <li key={i}>{source}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div className="bg-gray-100 p-4 rounded-lg mr-16">
            AI assistant is thinking...
          </div>
        )}
      </div>

      <form onSubmit={sendQuestion} className="flex gap-3">
        <input
          type="text"
          placeholder="Ask a follow-up question..."
          className="flex-1 border rounded-lg px-4 py-3"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button className="bg-blue-700 text-white px-6 rounded-lg">
          Send
        </button>
      </form>
    </div>
  );
}

export default ChatBox;