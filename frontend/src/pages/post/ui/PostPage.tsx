import { Post as PostType } from "@/shared/types/Post";
import Head from "next/head";

export default function Post({ post }: { post: PostType }) {
  const { seo, data } = post;
  return (
    <>
      <Head>
        <title>{seo.title}</title>
        <meta name="description" content={seo.meta_description} />

        {/* OpenGraph (Facebook, LinkedIn) */}
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
      <div>
        <h1>{data.title}</h1>
      </div>
    </>
  );
}
