import { GetServerSidePropsContext } from "next";
import { PostPage } from "@/pages/post";
// import posts from "@/shared/const/posts.json";
import { Post as PostType } from "@/shared/types/Post";
import PostProvider from "@/app/providers/Post/PostProvider";
import { checkSSRRateLimit } from "@/shared/lib/rateLimiter";

export async function getServerSideProps(
  context: GetServerSidePropsContext<{ id: string }>
) {
  const rateLimitResult = await checkSSRRateLimit(context.req);
  if (rateLimitResult.redirect) return rateLimitResult;

  const { id } = context.params!;

  // const post = posts.posts.find((post) => post.id === id);
  const res = await fetch(`http://localhost:8000/api/posts/${id}/`);
  const post = await res.json();

  if (!post || post.detail) {
    return { notFound: true };
  }

  return { props: { post } };
}

export default function Post({ post }: { post: PostType }) {
  return (
    <PostProvider>
      <PostPage post={post} />
    </PostProvider>
  );
}
