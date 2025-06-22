import Head from "next/head";

export default function Posts() {
  return (
    <>
      <Head>
        <title>Posts list</title>
        <meta name="description" content="Posts list description" />
      </Head>
      <div className={`min-h-[100vh]`}>
        <div className="container mx-auto px-4 pt-10">
          <h1 className="text-3xl font-bold text-gray-800 mb-8">
            Latest Posts
          </h1>
          <div className="space-y-8">
            <div className="p-6 bg-white rounded-lg shadow-md overflow-hidden transition-all duration-300 hover:shadow-lg">
              <div className="mb-4">
                <h3 className="text-2xl font-semibold text-gray-800 mb-2 hover:text-blue-600 transition-colors">
                  <a href="#">Post title</a>
                </h3>
              </div>
              <div className="flex items-center text-gray-500 text-sm">
                <span className="flex items-center mr-4">
                  <svg
                    className="w-4 h-4 mr-1"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                    />
                  </svg>
                  Dima
                </span>
                <span className="flex items-center">
                  <svg
                    className="w-4 h-4 mr-1"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                    />
                  </svg>
                  25.10.2024
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
