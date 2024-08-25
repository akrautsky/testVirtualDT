import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Order Online text', () => {
  render(<App />);
  const linkElement = screen.getByText(/Order Online/i);
  expect(linkElement).toBeInTheDocument();
});
