import Link from "next/link";

export default function Header() {
  return (
    <header className="sticky top-0 z-50 flex items-center justify-between bg-white px-8 py-4 shadow-md">
      <Link href="/" className="flex items-center gap-3 no-underline">
        <img src="/logo.svg" alt="Логотип" className="h-10 w-auto" />
        <h1 className="text-xl font-bold text-gray-800">FS Blog</h1>
      </Link>

      <nav className="hidden md:flex md:gap-6">
        <Link
          href="/"
          className="relative px-1 py-2 text-gray-600 transition-all hover:text-black"
        >
          Home
          <span className="absolute bottom-0 left-0 h-0.5 w-0 bg-blue-500 transition-all duration-300 hover:w-full"></span>
        </Link>
        <Link
          href="/posts"
          className="relative px-1 py-2 text-gray-600 transition-all hover:text-black"
        >
          Posts
          <span className="absolute bottom-0 left-0 h-0.5 w-0 bg-blue-500 transition-all duration-300 hover:w-full"></span>
        </Link>
        <Link
          href="/about"
          className="relative px-1 py-2 text-gray-600 transition-all hover:text-black"
        >
          About
          <span className="absolute bottom-0 left-0 h-0.5 w-0 bg-blue-500 transition-all duration-300 hover:w-full"></span>
        </Link>
      </nav>

      <div className="flex items-center gap-4">
        <button className="md:hidden">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6 text-gray-600"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>

        <div className="flex h-9 w-9 items-center justify-center rounded-full bg-gray-100 transition-all hover:bg-gray-200 hover:shadow-md">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5 text-gray-600"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
            />
          </svg>
        </div>
      </div>
    </header>
  );
}
