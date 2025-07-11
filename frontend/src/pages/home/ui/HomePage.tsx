import { Footer } from "@/widgets/Footer";
import { Header } from "@/widgets/Header";
import Head from "next/head";

export default function Home() {
  return (
    <>
      <Head>
        <title>Wagtail + NextJS</title>
      </Head>
      <div>
        <Header/>
        <h1>Home Page</h1>
        <Footer/>
      </div>
    </>
  );
}
