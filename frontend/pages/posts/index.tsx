import { PostsPage } from "@/pages/posts";
import { Post as PostType } from "@/shared/types/Post";
import { GetServerSidePropsContext } from "next";
import { checkSSRRateLimit } from "@/shared/lib/rateLimiter";

export async function getServerSideProps(
  context: GetServerSidePropsContext<{ id: string }>
) {
  const rateLimitResult = await checkSSRRateLimit(context.req);
  if (rateLimitResult.redirect) return rateLimitResult;

  const res = await fetch(`http://localhost:8000/api/posts/`);
  const posts = await res.json();

  return { props: { posts } };
}

export default function Post({ posts }: { posts: PostType[] }) {
  return <PostsPage posts={posts} />;
}
