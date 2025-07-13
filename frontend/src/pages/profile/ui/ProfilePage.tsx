import Head from "next/head";

export default function Profile() {
  const user = {
    name: "Иван Иванов",
    email: "ivan@example.com",
    avatar: "https://randomuser.me/api/portraits/men/1.jpg",
    bio: "Фронтенд разработчик, любитель React и Tailwind CSS",
  };

  const posts = [
    {
      id: 1,
      title: "Мой первый пост",
      content: "Сегодня я изучил основы Tailwind CSS...",
    },
    {
      id: 2,
      title: "Работа с React",
      content: "Поделюсь опытом создания хуков...",
    },
    {
      id: 3,
      title: "Взаимодействие с API",
      content: "Как правильно организовать запросы...",
    },
  ];

  return (
    <>
      <Head>
        <title>Profile</title>
      </Head>
      <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-3xl mx-auto">
          <div className="bg-white shadow rounded-lg overflow-hidden">
            <div className="bg-gradient-to-r from-blue-500 to-indigo-600 h-32"></div>
            <div className="px-6 py-4 flex items-center -mt-16">
              <div className="relative">
                <img
                  className="h-24 w-24 rounded-full border-4 border-white object-cover"
                  src={user.avatar}
                  alt="Аватар пользователя"
                />
                <span className="absolute bottom-0 right-0 bg-green-500 rounded-full w-6 h-6 border-2 border-white"></span>
              </div>
              <div className="ml-6">
                <h1 className="text-2xl font-bold text-gray-900">
                  {user.name}
                </h1>
                <p className="text-gray-600">{user.email}</p>
                <p className="mt-1 text-gray-500">{user.bio}</p>
              </div>
            </div>

            <div className="px-6 py-4 border-t border-gray-200">
              <div className="flex space-x-6">
                <div className="text-center">
                  <p className="text-gray-500">Посты</p>
                  <p className="text-lg font-semibold text-gray-900">42</p>
                </div>
                <div className="text-center">
                  <p className="text-gray-500">Подписчики</p>
                  <p className="text-lg font-semibold text-gray-900">1.2K</p>
                </div>
                <div className="text-center">
                  <p className="text-gray-500">Подписки</p>
                  <p className="text-lg font-semibold text-gray-900">87</p>
                </div>
              </div>
            </div>
          </div>

          <div className="mt-8">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">
              Мои посты
            </h2>
            <div className="space-y-6">
              {posts.map((post) => (
                <div
                  key={post.id}
                  className="bg-white shadow rounded-lg overflow-hidden"
                >
                  <div className="p-6">
                    <h3 className="text-lg font-medium text-gray-900">
                      {post.title}
                    </h3>
                    <p className="mt-2 text-gray-600">{post.content}</p>
                    <div className="mt-4 flex items-center text-sm text-gray-500">
                      <span>2 дня назад</span>
                      <span className="mx-2">·</span>
                      <span>15 лайков</span>
                      <span className="mx-2">·</span>
                      <span>3 комментария</span>
                    </div>
                  </div>
                  <div className="bg-gray-50 px-6 py-3 flex justify-between">
                    <button className="text-indigo-600 hover:text-indigo-500 font-medium">
                      Редактировать
                    </button>
                    <button className="text-red-600 hover:text-red-500 font-medium">
                      Удалить
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
