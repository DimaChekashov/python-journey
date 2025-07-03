export type PostProps = {
  title: string;
  content: string;
  author: string;
  date: string;
  tags?: string[];
};

export default function Post({
  title,
  content,
  author,
  date,
  tags = [],
}: PostProps) {
  return (
    <article className="bg-white rounded-lg shadow-md p-5 mb-5 max-w-3xl mx-auto">
      <header className="mb-4 pb-3 border-b border-gray-100">
        <h1 className="text-2xl font-bold text-gray-800 mb-1">{title}</h1>
        <div className="flex items-center text-sm text-gray-500 space-x-3">
          <span>By {author}</span>
          <span>{date}</span>
        </div>
      </header>

      <div className="prose prose-sm sm:prose-base max-w-none text-gray-700 mb-4">
        <p>{content}</p>
      </div>

      {tags?.length > 0 && (
        <footer className="mt-4 pt-3 border-t border-gray-100">
          <ul className="flex flex-wrap gap-2">
            {tags.map((tag, index) => (
              <li
                key={index}
                className="px-2.5 py-1 bg-gray-100 text-gray-600 text-xs rounded-full"
              >
                {tag}
              </li>
            ))}
          </ul>
        </footer>
      )}
    </article>
  );
}
