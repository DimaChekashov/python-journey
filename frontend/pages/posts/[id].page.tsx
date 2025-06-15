import { GetServerSidePropsContext } from "next";
import { PostPage } from "@/pages/post";
import posts from "@/shared/const/posts.json";
import { Post as PostType } from "@/shared/types/Post";

export async function getServerSideProps(
  context: GetServerSidePropsContext<{ id: string }>
) {
  const { id } = context.params!;
  
  const post = posts.posts.find((post) => post.id === id);

  if (!post) {
    return { notFound: true };
  }

  return { props: { post } };
}

export default function Post({ post }: { post: PostType }) {
  return <PostPage post={post} />;
}
