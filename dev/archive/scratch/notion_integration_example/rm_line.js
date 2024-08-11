import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_KEY });

(async () => {
  const blockId = '5397f7ff-e5df-4f22-8675-efc8ed0dc291';
  const response = await notion.blocks.delete({
    block_id: blockId,
  });
  console.log(response);
})();