import { Post as PostType } from "@/shared/types/Post";
import Head from "next/head";

export default function Post({ post }: { post: PostType }) {
  const { seo, data, template, status } = post;
  return (
    <>
      <Head>
        <title>{seo.title}</title>
        <meta name="description" content={seo.meta_description} />

        <meta property="og:title" content={seo.title} />
        <meta property="og:description" content={seo.meta_description} />
        <meta property="og:image" content={seo.og_image} />
        <meta property="og:url" content={seo.og_image} />
        <meta property="og:type" content="article" />

        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={seo.title} />
        <meta name="twitter:description" content={seo.meta_description} />
        <meta name="twitter:image" content={seo.og_image} />

        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="robots" content="index, follow" />
      </Head>
      <div className={`min-h-[100vh] template-${template}`}>
        <div className="container mx-auto px-4 pt-10">
          <h1 className="mb-6 text-3xl">{data.title}</h1>
          <article dangerouslySetInnerHTML={{ __html: data.content }} />
          <div className="flex gap-4 mt-6">
            <div>Автор: {data.author}</div>
            <div>Дата создания: {data.published_at}</div>
            <div>Просмотры: {data.views}</div>
          </div>
        </div>
      </div>
    </>
  );
}
