import Post, { PostProps } from "@/widgets/Post/ui/Post";

const mockPosts: PostProps[] = [
  {
    title: "Первая статья в блоге",
    content:
      "Это содержание моей первой статьи. Здесь я рассказываю о том, как начать работать с React и Tailwind CSS.",
    author: "Иван Иванов",
    date: "15 мая 2023",
    tags: ["react", "frontend"],
  },
  {
    title: "Продвинутые техники TypeScript",
    content:
      "В этой статье мы рассмотрим продвинутые паттерны TypeScript, которые помогут писать более надежный код.",
    author: "Петр Петров",
    date: "22 июня 2023",
    tags: ["typescript", "programming"],
  },
  {
    title: "Полное руководство по Next.js",
    content:
      "Next.js - это фреймворк React для производства. Узнайте, как использовать его в своих проектах.",
    author: "Мария Сидорова",
    date: "10 июля 2023",
    tags: ["nextjs", "react", "ssr"],
  },
];

export default function Posts() {
  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      <h1 className="text-3xl font-bold text-gray-800 mb-8">
        Последние статьи
      </h1>

      <div className="space-y-6">
        {mockPosts.map((post, index) => (
          <Post
            key={index}
            title={post.title}
            content={post.content}
            author={post.author}
            date={post.date}
            tags={post.tags}
          />
        ))}
      </div>

      <div className="mt-8 flex justify-center">
        <button className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors">
          Загрузить еще
        </button>
      </div>
    </div>
  );
}
