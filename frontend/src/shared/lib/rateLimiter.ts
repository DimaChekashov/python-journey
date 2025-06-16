// lib/rateLimiter.ts
import { RateLimiterMemory } from "rate-limiter-flexible";

const limiter = new RateLimiterMemory({
  points: 5, // 5 запросов
  duration: 60, // за 1 минуту
});

export const checkSSRRateLimit = async (req: any) => {
  const ip = req.headers["x-forwarded-for"] || req.connection.remoteAddress;
  try {
    await limiter.consume(ip);
    return { props: {} };
  } catch (err) {
    return {
      props: {},
      // Next.js 12+ позволяет возвращать redirect/notFound из getServerSideProps
      redirect: {
        destination: "/429",
        permanent: false,
      },
    };
  }
};
