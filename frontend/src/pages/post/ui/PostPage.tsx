import { Post as PostType } from "@/shared/types/Post";
import Head from "next/head";

export default function Post({ post }: { post: PostType }) {
  console.log(post);
  return (
    <>
      <Head>
        <title>POST</title>
      </Head>
      <div>
        <h1>Home Page</h1>
      </div>
    </>
  );
}
