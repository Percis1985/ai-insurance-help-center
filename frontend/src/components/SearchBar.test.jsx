import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import SearchBar from "./SearchBar";

test("calls onSearch when user searches", async () => {
  const mockSearch = vi.fn();

  render(<SearchBar onSearch={mockSearch} />);

  await userEvent.type(
    screen.getByPlaceholderText("Search insurance questions..."),
    "claim"
  );

  await userEvent.click(screen.getByText("Search"));

  expect(mockSearch).toHaveBeenCalledWith("claim");
});