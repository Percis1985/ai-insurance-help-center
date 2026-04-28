import { test, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import ArticleCard from "./ArticleCard";

test("renders article card details", () => {
  const article = {
    id: 1,
    title: "How to Submit a Claim",
    category: "Claims",
    content: "Submit documents and track your claim status.",
  };

  render(
    <BrowserRouter>
      <ArticleCard article={article} />
    </BrowserRouter>
  );

  expect(screen.getByText("Claims")).toBeInTheDocument();
  expect(screen.getByText("How to Submit a Claim")).toBeInTheDocument();
  expect(screen.getByText(/Submit documents/i)).toBeInTheDocument();
  expect(screen.getByText(/Read more/i)).toBeInTheDocument();
});